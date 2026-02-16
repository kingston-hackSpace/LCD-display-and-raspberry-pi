#include <Keyboard.h>
#include <KeyboardLayout.h>
#include <Keyboard_da_DK.h>
#include <Keyboard_de_DE.h>
#include <Keyboard_es_ES.h>
#include <Keyboard_fr_FR.h>
#include <Keyboard_it_IT.h>
#include <Keyboard_sv_SE.h>

// Define the number of rows and columns in the matrix
const int numRows = 4;

// Define the pins connected to the rows and columns of the matrix
const int rowPins[numRows] = {2, 3, 4, 5};   // Pins connected to the rows

// Define a 2D array to store the state of each button in the matrix
int buttonState[numRows][numCols];

// Define variables to store the previous state of each button
int prevButtonState[numRows][numCols];

// Create an Encoder object
Encoder encoder(encoderPinA, encoderPinB);

// Variables to store encoder position
long encoderPosition = 0;
long lastEncoderPosition = 0;

int counter = 0;
int aState;
int aLastState;

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);

  // Initialize the button matrix pins as INPUT_PULLUP
  for (int i = 0; i < numRows; i++) {
    pinMode(rowPins[i], OUTPUT);
    digitalWrite(rowPins[i], HIGH); // Pull-up resistors for the rows
  }
}

void loop() {

  // Read the state of each button in the matrix
  for (int row = 0; row < numRows; row++) {
    // Set current row to LOW to activate it
    digitalWrite(rowPins[row], LOW);
    
      // If the button state has changed from HIGH to LOW, register a button press
      if (buttonState[row] == LOW && prevButtonState[row] == HIGH) {
        Serial.print("Button Pressed at Row ");
        Serial.print(row + 1);
        Serial.print(", Column ");
        Serial.println(col + 1);
        sendKeyPress(row);
      }
      
      // Update the previous button state
      prevButtonState[row] = buttonState[row];
    }
    
    // Set current row back to HIGH
    digitalWrite(rowPins[row], HIGH);
  
  // Add a small delay to debounce the buttons
  delay(50);
}

void sendKeyPress(int key)
{
  switch(key)
  {
    case 1:  
      Keyboard.write('1');  // Sends a keyboard '1'
      break;
    case 2:  
      Keyboard.write('2');
      break;
    case 3:  
      Keyboard.write('3');
      break;
    case 4:  
      Keyboard.write('4');
      break;
  }
}
