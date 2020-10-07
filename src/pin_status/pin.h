#include <stdio.h>

typedef struct Pin{
    int pin_id;
    double duty_cycle;  
} Pin;

void print_pin(Pin* pin){
    printf("Pin ID: %d\nDuty Cycle: %f\n", pin->pin_id, pin->duty_cycle);   
}
