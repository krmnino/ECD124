#include "PinArray.h"

const int NUMBER_OF_PINS = 48;

int main(){
    PinArray* pin_array = init_arr(NUMBER_OF_PINS);
    print_arr(pin_array);
    sort_duty_cycles(pin_array);
}