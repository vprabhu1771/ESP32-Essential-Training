The **MQ-4 Gas Sensor** is designed to detect **Methane (CH₄) and Natural Gas**. It outputs both **analog (A0)** and **digital (D0)** signals, making it easy to interface with an **ESP32-WROOM**.

---

## **🔌 Wiring ESP32 with MQ-4 Sensor**
| MQ-4 Pin | ESP32 Pin |
|----------|----------|
| **VCC** | **5V** *(MQ-4 requires 5V for heating element)* |
| **GND** | **GND** |
| **A0 (Analog Output)** | **GPIO 34** *(or any ADC pin)* |
| **D0 (Digital Output)** | **GPIO 27** *(optional, for threshold-based alert)* |

> **⚠️ Note:** ESP32's ADC reads **0-3.3V**, while MQ-4 can output **up to 5V**. Use a **voltage divider** (4.7kΩ & 10kΩ) to step it down.

---

## **📜 ESP32 Code for MQ-4 (Analog Output - CH₄ Measurement)**
```cpp
#define MQ4_ANALOG_PIN 34  // ADC-capable pin

void setup() {
  Serial.begin(115200); // Start Serial Monitor
}

void loop() {
  int sensorValue = analogRead(MQ4_ANALOG_PIN);  // Read raw ADC value (0-4095 for ESP32)
  float voltage = sensorValue * (3.3 / 4095.0);  // Convert ADC value to voltage

  Serial.print("Raw ADC Value: ");
  Serial.print(sensorValue);
  Serial.print(" | Voltage: ");
  Serial.print(voltage);
  Serial.println("V");

  delay(1000); // 1-second delay
}
```

---

## **📜 ESP32 Code for MQ-4 (Digital Output - Gas Alert)**
If you want a **gas threshold alert**, use the **D0 pin** (connect to **GPIO 27**):

```cpp
#define MQ4_DIGITAL_PIN 27  // Digital output pin

void setup() {
  Serial.begin(115200);
  pinMode(MQ4_DIGITAL_PIN, INPUT);
}

void loop() {
  int gasDetected = digitalRead(MQ4_DIGITAL_PIN);
  
  if (gasDetected == LOW) {  // MQ-4 outputs LOW when gas level is high
    Serial.println("⚠️ Methane Gas Detected!");
  } else {
    Serial.println("✅ Air is Clean.");
  }

  delay(1000);
}
```

---

## **💨 MQ-4 Gas Sensor Behavior**
1. **Analog Output (A0):**  
   - **Higher Voltage** → More Methane (CH₄) detected.  
   - **Lower Voltage** → Less gas present.  

2. **Digital Output (D0):**  
   - **HIGH (1)** → Safe (No gas detected).  
   - **LOW (0)** → Dangerous gas level (Set threshold via potentiometer).

---

## **📊 Interpreting MQ-4 Readings**
| Voltage (V) | Methane Level |
|-------------|--------------|
| **< 1.0V**  | Clean Air |
| **1.0 - 2.0V** | Low CH₄ |
| **2.0 - 3.0V** | Moderate CH₄ |
| **> 3.0V**  | High CH₄ (Danger!) |

> **🔥 Improve Accuracy:**  
> ✅ Use a **calibrated formula** based on the sensor’s datasheet.  
> ✅ Apply **moving average filtering** for smooth readings.  
> ✅ Trigger an **alarm or IoT notification** (via WiFi, MQTT, or Firebase).

Let me know if you need modifications! 🚀