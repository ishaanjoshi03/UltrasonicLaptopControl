#include <SR04.h>
#include <SR04.h>



#define trigger1 2;
#define echo1 3;

SR04 sr04 = SR04(echo1,trigger1);
long distL;

void setup() {
  Serial.begin(9600);
  pinMode(trigger1, OUTPUT);
  pinMode(echo1, INPUT);
}

void loop() {
  distL = sr04.Distance();
  if (distL > 50 && distL < 60) {
    Serial.println("Rewind"); 
    delay(500);
  }
  if (distL >= 13 && distL <= 17) {
    delay(100);
    distL = sr04.Distance();
    if (distL >= 13 && distL <= 17) {
      Serial.println("Left locked");
      while(distL <= 40){
        distL = sr04.Distance();
        if (distL < 10){
          Serial.println("Vup");
          delay(300);
        }
        if (distL > 20){
          Serial.println("Vdown");
          delay(300);
        }
      }
    }
  }
}
