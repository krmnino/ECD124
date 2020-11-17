#include "i2c.hpp"
#include <stdio.h>

int main(){
    Session green_session;
    Session red_session;

    int ret = green_session.init_i2c(0x2);
    if(ret < 0){
	printf("Couldn't init i2c");
    }

    int ret2 = red_session.init_i2c(0x3);
    if(ret2 < 0){
	printf("Couldn't init i2c");
    }

    int ret3 = green_session.send_i2c("example");
    

    green_session.request_i2c();
    printf("Green: %s\n", green_session.msg_received);

    red_session.request_i2c();
    printf("Red: %s\n", red_session.msg_received);
}