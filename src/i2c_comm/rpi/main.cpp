#include "i2c.hpp"
#include <string>

int main(){
    Session i2c_session;
    std::string msg = "example";
    for(unsigned int i = 0; i < msg.size(); i++){
        i2c_session.msg_sent = msg[i];
        i2c_session.write_to(0x2);
    }
}