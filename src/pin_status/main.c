
#include "pinarray.h"


const int NUMBER_OF_PINS = 48;

int main(){
    PinArray* pin_array = init_arr(NUMBER_OF_PINS);
    print_arr(pin_array);
}