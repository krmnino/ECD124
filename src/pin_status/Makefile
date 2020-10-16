ifeq ($(DEBUG),1)
TARGET=pin_array
CC=gcc
CCFLAGS = -Wall -DDEBUG
HEADERS = Pin.h PinArray.h DebugUtil.h
else
TARGET=pin_array
CC=gcc
CCFLAGS = -Wall
HEADERS = Pin.h PinArray.h
endif

$(TARGET): main.o
	$(CC) $(CCFLAGS) -o $@ main.o

main.o: main.c $(HEADERS)
	$(CC) $(CCFLAGS) -O -c main.c

clean:
	rm main.o $(TARGET)