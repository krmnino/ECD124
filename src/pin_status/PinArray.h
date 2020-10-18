#ifndef DEBUG
#include "Pin.h"
#endif

#include <stdio.h>

#ifndef PINARR
#define PINARR

typedef struct PinArray{
    Pin* arr;
    size_t size;  
} PinArray;

PinArray* init_arr(size_t size_){
    PinArray* pin_array = (PinArray*)malloc(sizeof(PinArray));
    pin_array->size = size_;
    pin_array->arr = (Pin*)malloc(sizeof(Pin) * size_);
    if(pin_array->arr == NULL){
        return NULL;
    }
    int i;
    for(i = 0; i < size_; i++){
        init_pin(&pin_array->arr[i], i, 48-i, i % 2);
    }
    return pin_array;
}

void swap(Pin* p1, Pin* p2){
    Pin temp = *p1;
    *p1 = *p2;
    *p2 = temp;
    return;
}

//Sort pins by duty cycles using insertion sort
void sort_duty_cycles_IS(PinArray* pin_array){
    int i;
    for(i = 0; i < pin_array->size; i++){
        int j;
        for(j = 0; j < pin_array->size; j++){
            if(pin_array->arr[j].duty_cycle < pin_array->arr[j - 1].duty_cycle){
                swap(&pin_array->arr[j], &pin_array->arr[j - 1]);                
            }
        }
    }
    return;
}

//Sort pins by duty cycles using quick sort
int get_partition(Pin arr[], int start, int end){
    Pin pivot = arr[end];
    int i = (start - 1);
    int j;
    for(j = start; j <= end - 1; j++){
        if(arr[j].duty_cycle < pivot.duty_cycle){
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[end]);
    return (i + 1);
}

void sort_duty_cycles_QS(PinArray* pin_array, int start, int end){
    if(start >= end){
        return;
    }
    else{
        int partition = get_partition(pin_array->arr, start, end);
        sort_duty_cycles_QS(pin_array, start, partition - 1);
        sort_duty_cycles_QS(pin_array, partition + 1, end);
    }
}

#endif