```
https://www.youtube.com/watch?v=AitCKcyjHuQ
```

Yes — **you can absolutely program the ESP32 using C/C++ with the Arduino IDE** (or PlatformIO). MicroPython is just **one of the many ways** to program the ESP32 — not the only one.

---

### ✅ Ways to Program the ESP32

| Method        | Language       | Tools                     |
| ------------- | -------------- | ------------------------- |
| Arduino       | C/C++          | Arduino IDE, PlatformIO   |
| ESP-IDF       | C (native SDK) | ESP-IDF (Espressif tools) |
| MicroPython   | Python         | Thonny, uPyCraft, etc.    |
| CircuitPython | Python         | Mu editor, etc.           |
| Lua (NodeMCU) | Lua            | ESPlorer                  |

---

### 🚀 How to Program ESP32 with Arduino (C/C++)

#### 🔧 Step 1: Install Arduino IDE

* Download from [https://arduino.cc](https://www.arduino.cc/en/software)

#### 🔧 Step 2: Add ESP32 Board Support

1. Open Arduino IDE
2. Go to **File > Preferences**
3. In *"Additional Boards Manager URLs"*, paste this:

   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
4. Click OK.

#### 🔧 Step 3: Install ESP32 Boards

1. Go to **Tools > Board > Boards Manager**
2. Search for **ESP32** by Espressif
3. Click **Install**

#### 🔧 Step 4: Select Your ESP32 Board

* **Tools > Board > ESP32 Arduino > \[Your Board]** (e.g., "ESP32 Dev Module")

#### 🔧 Step 5: Install `ESP32-BLE-Gamepad` Library

1. Go to **Sketch > Include Library > Manage Libraries**
2. Search for `ESP32 BLE Gamepad`
3. Install the one by **lemmingDev**

#### 🔧 Step 6: Upload Code

1. Plug in your ESP32
2. Choose the correct port in **Tools > Port**
3. Click the **Upload** button (right-arrow icon)

---

### 🛠️ Troubleshooting Tips

* Hold the **BOOT** button on ESP32 while uploading if upload fails.
* Install the **CP2102/CH340 driver** if your ESP32 isn’t detected.

---

### ✅ Summary

Yes, ESP32 **fully supports programming in C/C++** via the **Arduino core** or the **ESP-IDF SDK**. You’re not limited to MicroPython.

If you want, I can give you a **complete button + joystick gamepad example** in Arduino C for ESP32.
