To blink an **external LED** using an **ESP32**, you need a simple circuit and a basic Arduino sketch.

---

### 🔧 **What You Need:**
- ESP32 board  
- 1x LED  
- 1x 220Ω resistor  
- Breadboard and jumper wires

---

### ⚡ **Circuit Setup:**
1. Connect **one end of the resistor** to GPIO pin (e.g., **GPIO 5**) on ESP32.
2. Connect the **other end of the resistor** to the **anode (+)** of the LED.
3. Connect the **cathode (-)** of the LED to **GND** on the ESP32.

```
ESP32 GPIO 5  ──┬──>──[220Ω]──>──|>|─── GND
                |               LED
               Pin
```

---

### 💻 **Arduino Code:**

```cpp
#define LED_PIN 5  // Use GPIO 5 (can change to any digital pin)

void setup() {
  pinMode(LED_PIN, OUTPUT); // Set the pin as output
}

void loop() {
  digitalWrite(LED_PIN, HIGH); // Turn LED on
  delay(1000);                 // Wait 1 second
  digitalWrite(LED_PIN, LOW);  // Turn LED off
  delay(1000);                 // Wait 1 second
}
```

---

### ✅ Notes:
- You can use **any GPIO pin** (except pins reserved for special use).
- Make sure **uploading the sketch** using the correct board settings:
  - **Board:** ESP32 Dev Module
  - **Port:** Select correct COM port
- If LED doesn’t blink, double-check the pin number and wiring.

Want a version for MicroPython too?