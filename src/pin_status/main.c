#include "Pin.h"

int main(){
    Pin array_pins[10];
    size_t array_size = sizeof(array_pins)/sizeof(array_pins[0]);
    for(int i = 0; i < sizeof(array_pins)/sizeof(array_pins[0]); i++){
        array_pins[i].pin_id = i; 
        array_pins[i].duty_cycle = 0.5;
    }
    print_array(array_pins, array_size);
}