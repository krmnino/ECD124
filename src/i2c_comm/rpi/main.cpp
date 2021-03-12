#include "i2c.hpp"
#include <stdio.h>

int main(){
    Session pi_session;

    int ret = pi_session.init_i2c(0x05);
    if(ret < 0){
	printf("Couldn't init master i2c device.");
    }

    int ret3 = pi_session.send_i2c("example");

    pi_session.request_i2c();
    printf("Pi: %s\n", pi_session.msg_received);
}