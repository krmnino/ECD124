#ifndef PINARRDEB
#define PINARRDEB

#include <stdio.h>
#include "Pin.h"
#include "PinArray.h"

void print_pin(Pin* pin){
    printf("Pin ID: %d\nDuty Cycle: %d\nToggle: %d\n", pin->pin_id, pin->duty_cycle, pin->toggle);   
}

void print_arr(PinArray* pin_array){
    for(int i = 0; i < pin_array->size; i++){
        print_pin(&pin_array->arr[i]);
    }
}

int pinid_reg(PinArray* pin_array, int index){
    int pin_id = pin_array->arr[index].pin_id;
    return pin_id;
}

int dutycycle_reg(PinArray* pin_array, int index){
    int duty_cycle = pin_array->arr[index].duty_cycle;
    return duty_cycle;
}

int toggle_reg(PinArray* pin_array, int index){
    int toggle = pin_array->arr[index].toggle;
    return toggle;
}

#endif