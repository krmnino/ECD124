TARGET=pin_array
CC=gcc
CCFLAGS = -Wall

$(TARGET): main.o
	$(CC) $(CCFLAGS) -o $@ main.o

main.o: main.c pin.h
	$(CC) $(CCFLAGS) -O -c main.c

clean:
	rm main.o $(TARGET)