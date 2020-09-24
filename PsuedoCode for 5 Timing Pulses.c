
#includes <ti_drivers>

void toggle(char port,char mask);
//Pulses over 2 ports
#define PORT_A 1
#define PORT_B 2
//Duty Cycles Defined
#define GPIO_20_Duty 128
#define GPIO_21_Duty 64
#define GPIO_40_Duty 196

void main(void){
	Device_init();
	Device_initGPIO();//Disables GPIO Locks on all ports and sets pullup resisters
	//Function to set Data Direction for outputs
	//initialize all GPIO registers in use to 0
	unsigned char i=0;//Max val 256? What's a char look like on this hardware
	while(1){
		if(i==GPIO_20_Duty)toggle(PORT_A,1<<20);
		if(i==GPIO_21_Duty)toggle(PORT_A,1<<21);
		if(i==GPIO_40_Duty)toggle(PORT_B,1<<8);
		i+=1;
		if(i==255){clearGPIORegA();clearGPIORegB();}

	}
	return;
}




void toggle(char port, char mask){
	switch(port){
		case PORT_A:
				TOGGLE_REG_A=(mask);//Placeholder for real name of A Port toggle register
			break;
		case PORT_B:
				REG_B=(mask);
			break;
	}
}