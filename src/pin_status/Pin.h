#ifndef PIN
#define PIN

#include <stdlib.h>

typedef struct Pin{
    int pin_id;
    int duty_cycle;
    int toggle;
} Pin;

void init_pin(Pin* pin, int pin_id_, double duty_cycle_, int toggle_){
    pin->pin_id = pin_id_;
    pin->duty_cycle = duty_cycle_;
    pin->toggle = toggle_
}

Pin* create_pin(int pin_id_, int duty_cycle_, int toggle_){
    Pin* pin = (Pin*)malloc(sizeof(Pin));
    pin->pin_id = pin_id_;
    pin->duty_cycle = duty_cycle_;
    pin->toggle = toggle_;
    return pin;
}

#endif