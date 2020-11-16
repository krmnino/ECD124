#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <stdint.h>
#include <fcntl.h>
#include <unistd.h>

class Session{
private:
public:
    int fd;
    uint8_t curr_slave;
    uint8_t msg_received;
    uint8_t msg_sent;

    Session();
    ~Session();
    int init_i2c();
    int read_from(uint8_t, uint8_t);
    int write_to(uint8_t);
};

Session::Session(){}

Session::~Session(){}

int Session::init_i2c(){
    this->fd = open("/dev/i2c-1", O_RDWR);
    return this->fd;
} 

int Session::read_from(uint8_t addr, uint8_t data){
    if(ioctl(this->fd, I2C_SLAVE, addr) < 0){
        return -1;
    }
    if(read(fd, &this->msg_received, 1) != 1){
        return -1;
    }
    return 0;
}

int Session::write_to(uint8_t addr){
    if(ioctl(this->fd, I2C_SLAVE, addr) < 0){
        return -1;
    }
    if(write(fd, &this->msg_sent, 2) != 1){
        return -1;
    }
    return 0;
}