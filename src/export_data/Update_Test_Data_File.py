import random
import datetime
import time

from CSV_Parser import Table

def write_new_data(test_data, fields):
    new_data = {}
    latest_entry = test_data.get_latest_entry()
    for i in test_data.get_fields():
        if(i == 'Date'):
            date_now = datetime.datetime.strptime(latest_entry['Date'], "%Y-%m-%d %H:%M:%S")
            date_now += datetime.timedelta(0, 5)
            new_data[i] = datetime.datetime.strftime(date_now, '%Y-%m-%d %H:%M:%S')
            continue
        else:
            new_data[i] = random.randrange(fields[i][0], fields[i][1] + 1, 1)
    test_data.append_entry(new_data)

def run(path, fields, sleep_time):
    while(True):
        test_data = Table(path, mode='t')
        write_new_data(test_data, fields)
        test_data.save_as_csv(path)
        print('Updated file. Sleep for', sleep_time, 'seconds')
        time.sleep(sleep_time)

path = './data/test_data.csv'
sleep_time = 5
fields = {
    'Battery_Voltage' : (200, 500),
    'Battery_Current' : (10, 70),
    'Battery_Max_Discharge_Power' : (0, 200),
    'Battery_Max_Regen_Power' : (0, 200),
    'Battery_State' : (0, 5),
    'Battery_Temperature' : (0, 200),
    'WEMS_Target_Power' : (0, 100),
    'WEMS_Power_Direction' : (0, 1),
}

run(path, fields, sleep_time)