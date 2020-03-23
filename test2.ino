#include <RH_ASK.h>
#include <SPI.h> 

RH_ASK rf_driver(2000,6,5,4,false);

int buttonPin1 = 30;
int buttonPin2 = 26;
int buttonPin3 = 28;
int buttonPin4 = 32;

int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;
int buttonState4 = 0;
void setup()
{
    // Initialize ASK Object
    rf_driver.init();
    pinMode(buttonPin1,INPUT);
    pinMode(buttonPin2,INPUT);
    pinMode(buttonPin3,INPUT);
    pinMode(buttonPin4,INPUT);
    Serial.begin(9600);
}
 
void loop()
{
    buttonState1 = digitalRead(buttonPin1);
    buttonState2 = digitalRead(buttonPin2);
    buttonState3 = digitalRead(buttonPin3);
    buttonState4 = digitalRead(buttonPin4);
    const char *msg1 = "1";
    const char *msg2 = "2";
    const char *msg3 = "3";
    const char *msg4 = "4";
    const char *msg0 = "0";

    if(buttonState1 == HIGH){
      rf_driver.send((uint8_t *)msg1, strlen(msg1));
      rf_driver.waitPacketSent();
      delay(100);
    }

    else if(buttonState2 == HIGH){
      rf_driver.send((uint8_t *)msg2, strlen(msg2));
      rf_driver.waitPacketSent();
      delay(100);
    }

    else if(buttonState3 == HIGH){
      rf_driver.send((uint8_t *)msg3, strlen(msg3));
      rf_driver.waitPacketSent();
      delay(100);
    }

    else if(buttonState4 == HIGH){
      rf_driver.send((uint8_t *)msg4, strlen(msg4));
      rf_driver.waitPacketSent();
      delay(100);
    }

    else{
      rf_driver.send((uint8_t *)msg0, strlen(msg0));
      rf_driver.waitPacketSent();
      delay(100);
      //Serial.println("Done");
    }
}
