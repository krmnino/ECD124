#ifdef DEBUG
#include "DebugUtil.h"
#else
#include "PinArray.h"
#endif

const int NUMBER_OF_PINS = 48;

int main(){
    PinArray* pin_array = init_arr(NUMBER_OF_PINS);
    randomize_duty_cycles(pin_array, 1, 1000);
    sort_duty_cycles_QS(pin_array, 0, pin_array->size - 1);
    print_arr(pin_array);
    //print_pin(&pin_array->arr[30]);
}