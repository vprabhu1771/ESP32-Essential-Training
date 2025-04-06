```
// Set the pin for the built-in LED
const int ledPin = 2;  // Most ESP32 boards have the built-in LED on GPIO2

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn the LED on (HIGH is the voltage level)
  digitalWrite(ledPin, HIGH);
  
  // Wait for 1 second (1000 milliseconds)
  delay(1000);
  
  // Turn the LED off (LOW is the voltage level)
  digitalWrite(ledPin, LOW);
  
  // Wait for 1 second
  delay(1000);
}
```