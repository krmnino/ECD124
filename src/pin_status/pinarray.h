#include <stdio.h>
#include "stdlib.h"

#include "pin.h"

typedef struct PinArray{
    Pin* arr;
    size_t length;  
} PinArray;

PinArray* init_arr(size_t size_){
    PinArray* pin_array = (PinArray*)malloc(sizeof(PinArray));
    pin_array->length = size_;
    pin_array->arr = (Pin*)malloc(sizeof(Pin) * size_);
    if(pin_array->arr == NULL){
        printf("Error allocating space.");
        return NULL;
    }
    for(int i = 0; i < size_; i++){
        pin_array->arr[i].pin_id = i; 
        pin_array->arr[i].duty_cycle = 0.5;
    }
    return pin_array;
}

void print_arr(PinArray* print_array){
    PinArray deallocate = *print_array;
    for(int i = 0; i < deallocate.length; i++){
        print_pin(&deallocate.arr[i]);
    }
}