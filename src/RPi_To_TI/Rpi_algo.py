#RPi Control Algorithm
import RPi.GPIO as GPIO
import time
#Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #Status Input
STATUS_IN=21
GPIO.setup(20, GPIO.OUT) #Power Direction Output
POWER_DIRECTION=20
GPIO.setup(16, GPIO.OUT) #Power Magnitude Output
POWER_MAG_6=16
GPIO.setup(12, GPIO.OUT) #Power Magnitude Output
POWER_MAG_5=12
GPIO.setup(7, GPIO.OUT) #Power Magnitude Output
POWER_MAG_4=7
GPIO.setup(8, GPIO.OUT) #Power Magnitude Output
POWER_MAG_3=8
GPIO.setup(26, GPIO.OUT) #Power Magnitude Output
POWER_MAG_2=26
GPIO.setup(19, GPIO.OUT) #Power Magnitude Output
POWER_MAG_1=19
GPIO.setup(13, GPIO.OUT) #Power Magnitude Output
POWER_MAG_0=13
GPIO.setup(5, GPIO.OUT) #Status Output
STATUS_OUT=5
GPIO.setup(11, GPIO.OUT) #Lock Output
LOCK=11
#Globals to be included in Final Script
AC_CONNECTED=0
BATTERY_CONNECTED=0
WEMS_CONNECTED=0
BMS_CONNECTED=0
SAFE_TO_DISCONNECT=0
timeOut=5 #How long to wait for RPi response before assuming failure
CHARGER_STATUS = 1
BATTERY_STATUS = 1
BATTERY_HIGH_TEMP = 5
BATTERY_LOW_TEMP = 5
BATTERY_STATE_OF_CHARGE = 50
TARGET_POWER = 1
BATTERY_VOLTAGE_LIMIT = 5
MAX_BATTERY_DISCHARGE_CURRENT = 20
MAX_BATTERY_CHARGE_CURRENT = 20
BMS_POWER_CHARGE = BATTERY_VOLTAGE_LIMIT * MAX_BATTERY_CHARGE_CURRENT
BMS_POWER_DISCHARGE = BATTERY_VOLTAGE_LIMIT * MAX_BATTERY_DISCHARGE_CURRENT
MODE=1 #1 means charging 0 means discharging
# ------------------------------------------------------------
#Power direction (from WEMS) is not relevant to managing the magnitude of power

def TI_Handshake(): #retcode 0 = success, 1=Handshake startup fail 2=AC connection fail, 3=Battery connection fail
	global AC_CONNECTED
	global BMS_CONNECTED
	GPIO.output(STATUS_OUT,1) #Sets Pin 40 (GPIO 21) to a 1
	fail=wait()
	if fail:
		print('No Response')
		return 1 #error in handshake
	#TI has started up - Handshake begins
	print('Handshake Beginning')
	fail=wait()
	if fail:
		print('Battery Connection Failure')
		return 2 #TI should not be done yet
	AC_CONNECTED=1 #First pulse indicates AC Power connected
	print('AC Connected')
	fail=wait()
	if fail:
		print('Battery Connection Failure')
		return 3 #TI should not be done yet
	BATTERY_CONNECTED=1
	print('Battery Connected')
	GPIO.output(STATUS_OUT,1)
	return 0
def TI_Shutdown():
	global SAFE_TO_DISCONNECT
	GPIO.output(STATUS_OUT,0) #Sets status bit to 0 to indicate shutdown
	while(GPIO.input(STATUS_IN)):
		print('Wait to disconnect')
		time.sleep(2)
	SAFE_TO_DISCONNECT=1
	print('Safe to disconnect')
def wait(): #Waits for Pulse from TI and sends response when it recieves a pulse
	start=time.time()
	while GPIO.input(STATUS_IN) == 0:
		if (time.time()-start > timeOut):
			return 1 #RPi took too long to respond
	GPIO.output(STATUS_OUT,0)
	while GPIO.input(STATUS_IN) == 1:
		time.sleep(1)
	GPIO.output(STATUS_OUT,1)
	return 0
def toBinary(percent):
	binary = [0,0,0,0,0,0,0]
	for x in range(len(binary)):
		binary[x]=((1<<x) & percent) >> x
	return binary
def sendBinary(outputs):
	pins = [POWER_MAG_0, POWER_MAG_1, POWER_MAG_2, POWER_MAG_3, POWER_MAG_4, POWER_MAG_5, POWER_MAG_6]
	if len(pins) != len(outputs):
		print("length of output does not equal length of pin array. Exiting")
		return -1
	GPIO.output(LOCK,1)
	for x in range(len(outputs)):
		GPIO.output(pins[x],outputs[x])
	GPIO.output(LOCK,0)
	return 0
def SendChargeMag():
	GPIO.output(POWER_DIRECTION,1)
	sendBinary(toBinary(TARGET_POWER))
	return
def SendDischargeMag():
	GPIO.output(POWER_DIRECTION,0)
	sendBinary(toBinary(TARGET_POWER))
	return
def chargeBattery():
	global TARGET_POWER
	if BATTERY_STATE_OF_CHARGE < 100: #Only when all these conditions are met, can the batteries begin to be charged or discharged
		print("Battery has room to charge!")
		if TARGET_POWER > BMS_POWER_CHARGE:
			TARGET_POWER = BMS_POWER_CHARGE
			SendChargeMag()
			print("Target power from WEMS reduced to: ",TARGET_POWER)
		else:
			SendChargeMag()
			print("Target power from WEMS unchanged: Charge Target Power: ",TARGET_POWER)
	else:
		TARGET_POWER = 0
		print("Battery has no room to charge! No power exchange will occur.\n")
def dischargeBattery():
	global TARGET_POWER
	if BATTERY_STATE_OF_CHARGE >10:
		print("Battery has power to discharge")
		if TARGET_POWER > BMS_POWER_DISCHARGE:
			TARGET_POWER = BMS_POWER_DISCHARGE
			SendDischargeMag()
			print("Target power from WEMS reduced to: ",TARGET_POWER)
		else:
			SendDischargeMag()
			print("Target power from WEMS unchanged:Discharge Target Power: ",TARGET_POWER)

def write_statuses(BMS_CONNECTED, WEMS_CONNECTED, AC_CONNECTED, BATTERY_CONNECTED):
	with open('../GUI_App/data/Connection_Status.dat', 'w') as file:
		file.write('bms_status=' + str(BMS_CONNECTED) + '\n') 
		file.write('wems_status=' + str(WEMS_CONNECTED) + '\n') 
		file.write('ac_power_status=' + str(AC_CONNECTED) + '\n') 
		file.write('battery_status=' + str(BATTERY_CONNECTED) + '\n') 
try:
	retCode=TI_Handshake()
	print ("Retcode was ", retCode)
	if retCode:
		print("No response, shutting down please check connections and try again")
		GPIO.cleanup()
		quit()
	time.sleep(2)
	while GPIO.input(STATUS_IN):
		#Update BMS Variables
		TARGET_POWER=85
		print("Sending powerMag: ",TARGET_POWER)
		print("Power direction is: ",MODE)
		#Update WEMS Variables
		if CHARGER_STATUS == 1 and BATTERY_STATUS == 1:
			print("Charger status and battery status good!")
			if BATTERY_HIGH_TEMP <= 50 and BATTERY_LOW_TEMP >= 0:
				print("Battery temperature safe!")
				if MODE==1:
					chargeBattery()
				else:
					dischargeBattery()
			else:
				TARGET_POWER = 0
				chargeBattery() # sets power target on TI to 0
				print("Battery temperature dangerous! No power exchange will occur.\n")
		else:
			TARGET_POWER = 0
			chargeBattery() #Sets power target on TI to 0
			print("Charger status or battery status bad! No power exchange will occur.\n")
		write_statuses(BMS_CONNECTED, WEMS_CONNECTED, AC_CONNECTED, BATTERY_CONNECTED)
		time.sleep(3)
	print("Error. Shutting Down")
	GPIO.cleanup()
except KeyboardInterrupt:
	TI_Shutdown()
	GPIO.cleanup() #Resets all ports as inputs to protect them
