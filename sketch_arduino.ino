// initialize the library with the numbers of the interface pins
#include <LiquidCrystal.h>
LiquidCrystal lcd(13,12,7,6,5,3);

int Contrast=20;

int x = 500;

void setup() {
	// set up the LCD's number of columns and rows:
	lcd.begin(16,2);
	// clear the LCD screen:
	lcd.clear();
        lcd.print("Hello");
        analogWrite(10,Contrast);
        Serial.begin(9600);
}

void loop() {
  // when characters arrive over the serial port...
  if (Serial.available()) {
    // wait a bit for the entire message to arrive
    delay(100);
    // clear the screen
    lcd.clear();
    // read all the available characters
    while (Serial.available() > 0) {
      // display each character to the LCD
      lcd.write(Serial.read());
    }
  }
}