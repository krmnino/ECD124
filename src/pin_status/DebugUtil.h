#ifndef PINARRDEB
#define PINARRDEB

#include <stdio.h>
#include "Pin.h"
#include "PinArray.h"

void print_pin(Pin* pin){
    printf("Pin ID: %d\nDuty Cycle: %f\n", pin->pin_id, pin->duty_cycle);   
}

void print_arr(PinArray* pin_array){
    for(int i = 0; i < pin_array->size; i++){
        print_pin(&pin_array->arr[i]);
    }
}

#endif