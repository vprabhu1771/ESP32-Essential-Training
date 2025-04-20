```cpp
#define MQ2_PIN 34          // Use a safe ADC pin like GPIO34
#define BUZZER_PIN 27       // Buzzer pin
#define THRESHOLD 75       // Adjust based on testing
#define WARMUP_TIME 120     // Warm-up time in seconds
#define LED_BUILTIN 2     // Warm-up time in seconds

void setup() {
  Serial.begin(115200);
  pinMode(MQ2_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  Serial.println("MQ2 Sensor Warming Up...");

  // Warm-up countdown
  for (int i = WARMUP_TIME; i > 0; i--) {
    Serial.print("Warming up: ");
    Serial.print(i);
    Serial.println("s remaining");
    delay(1000);
  }

  Serial.println("✅ Sensor Warmed Up. Starting Gas Detection...");
}

void loop() {
  int sensorValue = analogRead(MQ2_PIN);
  Serial.print("Gas Sensor Value: ");
  Serial.println(sensorValue);

  if (sensorValue > THRESHOLD) {
    Serial.println("🔥 Gas Detected!");
    digitalWrite(BUZZER_PIN, HIGH);
  } else {
    Serial.println("✅ Safe Air");
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(BUZZER_PIN, LOW);
  }

  delay(1000);
}
```