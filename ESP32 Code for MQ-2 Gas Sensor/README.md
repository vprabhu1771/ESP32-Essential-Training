The **MQ-2 gas sensor** can detect **LPG, smoke, alcohol, propane, hydrogen, methane, and carbon monoxide**. It outputs both **analog** and **digital** signals, and you can interface it with an **ESP32-WROOM** to measure gas concentration.

---

### **Wiring ESP32 with MQ-2**
| MQ-2 Pin | ESP32 Pin |
|----------|----------|
| **VCC** | **3.3V or 5V** *(Use 5V for better accuracy)* |
| **GND** | **GND** |
| **A0 (Analog Output)** | **GPIO 34** *(or any ADC-capable pin)* |
| **D0 (Digital Output)** | **GPIO 27** *(or any digital pin, optional)* |

---

### **ESP32 Code for MQ-2 (Using Analog Output)**
```cpp
#define MQ2_ANALOG_PIN 34  // Use an ADC-capable pin on ESP32

void setup() {
  Serial.begin(115200); // Start Serial Monitor
}

void loop() {
  int sensorValue = analogRead(MQ2_ANALOG_PIN);  // Read raw ADC value (0-4095 for ESP32)
  float voltage = sensorValue * (3.3 / 4095.0);  // Convert to voltage

  Serial.print("Raw ADC Value: ");
  Serial.print(sensorValue);
  Serial.print(" | Voltage: ");
  Serial.print(voltage);
  Serial.println("V");

  delay(1000);  // Wait 1 second
}
```

---

### **MQ-2 Digital Output (Optional)**
If you want a **threshold-based alert**, use the **D0 pin** (connect to **GPIO 27**).

```cpp
#define MQ2_DIGITAL_PIN 27  // Digital output pin

void setup() {
  Serial.begin(115200);
  pinMode(MQ2_DIGITAL_PIN, INPUT);
}

void loop() {
  int gasDetected = digitalRead(MQ2_DIGITAL_PIN);
  
  if (gasDetected == LOW) {  // MQ-2 outputs LOW when gas exceeds threshold
    Serial.println("⚠️ Gas Detected!");
  } else {
    Serial.println("✅ Air is Clean.");
  }

  delay(1000);
}
```

---

### **How MQ-2 Works**
1. **Analog Output (A0):** Provides a voltage that varies with gas concentration.
2. **Digital Output (D0):** Goes LOW when gas level exceeds a preset threshold (adjustable using the onboard potentiometer).

---

### **Possible Improvements**
✅ **Calibrate sensor** using a known gas concentration.  
✅ Apply **moving average filtering** for stable readings.  
✅ **Trigger an alarm (buzzer or LED)** when gas is detected.  
✅ Send alerts via **WiFi (MQTT, HTTP, Firebase, or OneSignal notifications).**

Let me know if you need modifications! 🚀