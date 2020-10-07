
#include "pinarray.h"


const int NUMBER_OF_PINS = 48;

int main(){
    PinArray* pin_array = init_arr(NUMBER_OF_PINS);
    print_arr(pin_array);
    /*
    Pin array_pins[10];
    size_t array_size = sizeof(array_pins)/sizeof(array_pins[0]);
    for(int i = 0; i < sizeof(array_pins)/sizeof(array_pins[0]); i++){
        array_pins[i].pin_id = i; 
        array_pins[i].duty_cycle = 0.5;
    }
    Pin test;
    test.pin_id = 99;
    test.duty_cycle = 0.5;
    print(&test);
    print_array(array_pins, array_size);
    */
}