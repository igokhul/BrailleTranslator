// Include necessary libraries
#include <Arduino.h>

// Define the pins for the solenoid actuators
#define SOLENOID_PIN_1 2
#define SOLENOID_PIN_2 3
#define SOLENOID_PIN_3 4
#define SOLENOID_PIN_4 5
#define SOLENOID_PIN_5 6
#define SOLENOID_PIN_6 7
// Define the Braille character mappings
const byte brailleChars[26] = {
  B000000, // A
  B010000, // B
  B011000, // C
  B010010, // D
  B001000, // E
  B011010, // F
  B011110, // G
  B010100, // H
  B001010, // I
  B000110, // J
  B010101, // K
  B011101, // L
  B100100, // M
  B101100, // N
  B101000, // O
  B110100, // P
  B111100, // Q
  B110110, // R
  B101010, // S
  B111010, // T
  B100110, // U
  B101110, // V
  B110011, // W
  B010111, // X
  B011111, // Y
  B110101  // Z
};

void setup() {
  // Set up the solenoid actuators
  pinMode(SOLENOID_PIN_1, OUTPUT);
  pinMode(SOLENOID_PIN_2, OUTPUT);
  pinMode(SOLENOID_PIN_3, OUTPUT);
  pinMode(SOLENOID_PIN_4, OUTPUT);
  pinMode(SOLENOID_PIN_5, OUTPUT);
  pinMode(SOLENOID_PIN_6, OUTPUT);
}

void loop() {
  // Input the English text to convert
  String inputText = "HELLO WORLD"; // Replace with your input text
  
  // Convert the input text to Braille text
  String brailleText = "";
  for (int i = 0; i < inputText.length(); i++) {
    char c = inputText.charAt(i);
    if (c >= 'A' && c <= 'Z') {
      brailleText += (char)(brailleChars[c - 'A'] + '0');
    } else {
      brailleText += c;
    }
  }

  // Trigger solenoid actuators based on Braille text
  for (int i = 0; i < brailleText.length(); i++) {
    char c = brailleText.charAt(i);
    digitalWrite(SOLENOID_PIN_1, bitRead(c, 0));
    digitalWrite(SOLENOID_PIN_2, bitRead(c, 1));
    digitalWrite(SOLENOID_PIN_3, bitRead(c, 2));
    digitalWrite(SOLENOID_PIN_4, bitRead(c, 3));
    digitalWrite(SOLENOID_PIN_5, bitRead(c, 4));
    digitalWrite(SOLENOID_PIN_6, bitRead(c, 5));
    delay(1000); // Delay for solenoid activation, adjust as needed
    digitalWrite(SOLENOID_PIN_1, HIGH);
    digitalWrite(SOLENOID_PIN_2, HIGH);
    digitalWrite(SOLENOID_PIN_3, HIGH);
    digitalWrite(SOLENOID_PIN_4, HIGH);
    digitalWrite(SOLENOID_PIN_5, HIGH);
    digitalWrite(SOLENOID_PIN_6, HIGH);
    delay(500); // Delay between characters, adjust as needed
  }
}