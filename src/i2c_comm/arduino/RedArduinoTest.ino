#include <Wire.h>

int register_selector = 0;

const char* req = "bits";
String received = "";

void setup() {  
  Wire.begin(0x3);
  Wire.onReceive(receive_handler);
  Wire.onRequest(request_handler);
  Serial.begin(9600);
}

void loop() {
  delay(100);
  Serial.println(received);
  received = "";
}

void receive_handler(int bytes){
  String data = "";
  while(Wire.available()){
    data += (char)Wire.read();
  }
  received += data;
}

void request_handler(){  
  Wire.write(req);
}