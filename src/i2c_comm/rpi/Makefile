TARGET=i2c_rpi
CC=g++
CCFLAGS = -Wall
HEADERS = i2c.hpp

$(TARGET): main.o
	$(CC) $(CCFLAGS) -o $@ main.o

main.o: main.cpp $(HEADERS)
	$(CC) $(CCFLAGS) -O -c main.cpp

clean:
	rm main.o $(TARGET)