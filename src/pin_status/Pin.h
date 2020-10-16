#ifndef PIN
#define PIN

#include <stdlib.h>

typedef struct Pin{
    int pin_id;
    double duty_cycle;  
} Pin;

void init_pin(Pin* pin, int pin_id_, double duty_cycle_){
    pin->pin_id = pin_id_;
    pin->duty_cycle = duty_cycle_;
}

Pin* create_pin(int pin_id_, double duty_cycle_){
    Pin* pin = (Pin*)malloc(sizeof(Pin));
    pin->pin_id = pin_id_;
    pin->duty_cycle = duty_cycle_;
    return pin;
}

#endif