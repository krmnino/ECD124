#include <stdio.h>

typedef struct Pin{
    int pin_id;
    double duty_cycle;  
} Pin;

void print(Pin* pin){
    printf("Pin ID: %d\nDuty Cycle: %f\n", pin->pin_id, pin->duty_cycle);   
}

void print_array(Pin arr[], size_t n){
    for(int i = 0; i < n; i++){
        print(&arr[i]);
    }
}