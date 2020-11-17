#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>
#include <cstring>

#include <stdio.h>

class Session{
private:
    int fd;
    uint8_t addr;
public:
    char msg_received[256] = {0};

    Session();
    ~Session();
    int init_i2c(uint8_t);
    int get_file_descriptor();
    uint8_t get_address();
    int request_i2c();
    int send_i2c(const char* msg);
};

Session::Session(){}

Session::~Session(){
    if(this->fd){
        close(fd);
    }
}

int Session::get_file_descriptor(){
    return this->fd;
}

uint8_t Session::get_address(){
    return this->addr;
}

int Session::init_i2c(uint8_t addr){
    this->fd = open("/dev/i2c-1", O_RDWR);
    if(this->fd < 0){
        return -1;
    }
    this->addr = addr;
    if(ioctl(this->fd, I2C_SLAVE, this->addr) < 0){
        return -1;
    }
    return 0;
} 

int Session::request_i2c(){
    if(read(this->fd, &this->msg_received, 256) != 1){
        return -1;
    }
    return 0;
}

int Session::send_i2c(const char* msg){
    int msg_char = 0;
    for(unsigned int i = 0; i < strlen(msg); i++){
        msg_char = msg[i];
	if(write(this->fd, &msg_char, 2) < 0){
	    return -1;
        }
    }
    return 0;
}
