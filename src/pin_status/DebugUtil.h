#ifndef PINARRDEB
#define PINARRDEB

#include <stdio.h>
#include <time.h>
#include "Pin.h"
#include "PinArray.h"

void print_pin(Pin* pin){
    printf("Pin ID: %d\nDuty Cycle: %d\nToggle: %d\n", pin->pin_id, pin->duty_cycle, pin->toggle);   
    return;
}

void print_arr(PinArray* pin_array){
    for(int i = 0; i < pin_array->size; i++){
        print_pin(&pin_array->arr[i]);
    }
    return;
}

void randomize_duty_cycles(PinArray* pin_array, int lower_range, int upper_range){
    srand(time(0));
    for(int i = 0; i < pin_array->size; i++){
        int rand_num = rand() % (upper_range - lower_range + 1) + lower_range;
        pin_array->arr[i].duty_cycle = rand_num;
    }
    return;
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