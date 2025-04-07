The **DFRobot SEN0189 Turbidity Sensor** can be connected to an **ESP32-WROOM** to measure water clarity. This sensor outputs an **analog voltage** corresponding to the water’s turbidity. The **ESP32 ADC (Analog-to-Digital Converter)** reads this voltage, which you can then convert into **NTU (Nephelometric Turbidity Units).**

---

### **Connections:**
| SEN0189 Pin | ESP32 Pin |
|-------------|----------|
| **VCC** (+5V) | **5V** |
| **GND** | **GND** |
| **A0 (Analog Output)** | **GPIO 34** (or any ADC pin) |

> 🛑 **ESP32 is a 3.3V device!** The sensor uses 5V, but its **analog output must not exceed 3.3V**. Use a **voltage divider (2.2kΩ & 4.7kΩ)** or **a level shifter** to step down the voltage.

---

### **ESP32 Code for Turbidity Sensor**
```cpp
#define TURBIDITY_SENSOR_PIN 34  // Use an ADC-capable pin

void setup() {
  Serial.begin(115200); // Start Serial Monitor
}

void loop() {
  int sensorValue = analogRead(TURBIDITY_SENSOR_PIN);  // Read raw ADC value (0-4095 for ESP32)
  float voltage = sensorValue * (3.3 / 4095.0);        // Convert to voltage
  float NTU = map(sensorValue, 0, 4095, 3000, 0);      // Adjust for sensor calibration

  Serial.print("Raw ADC Value: ");
  Serial.print(sensorValue);
  Serial.print(" | Voltage: ");
  Serial.print(voltage);
  Serial.print("V | Turbidity: ");
  Serial.print(NTU);
  Serial.println(" NTU");

  delay(1000); // Wait 1 second
}
```

---

### **How It Works:**
1. Reads the **analog voltage** from the sensor.
2. Converts it into a **voltage value** (ESP32 ADC range is **0-3.3V**).
3. Uses **basic mapping** for NTU estimation. A more **precise calibration** may be needed.

---

### **Turbidity Ranges (Approximate NTU)**
| NTU Value | Water Condition |
|-----------|----------------|
| **0-50**  | Clean Water |
| **50-100** | Slightly Cloudy |
| **100-500** | Moderately Cloudy |
| **500+** | Very Turbid |

---
### **Possible Improvements**
✅ Use **calibration** by measuring a known sample.  
✅ Use **median filtering** to smooth ADC noise.  
✅ Log data to an **SD card** or **send it via WiFi** using MQTT/HTTP.

Let me know if you need modifications! 🚀