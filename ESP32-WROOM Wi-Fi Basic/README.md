The **ESP32-WROOM** is a powerful Wi-Fi and Bluetooth module developed by Espressif. Here's a quick overview focused on its **Wi-Fi** capabilities:

---

### 🔌 ESP32-WROOM Wi-Fi Features

| Feature                | Details                                                                 |
|------------------------|-------------------------------------------------------------------------|
| **Wi-Fi Standard**     | IEEE 802.11 b/g/n (2.4 GHz only)                                        |
| **Modes**              | Station (STA), Soft Access Point (AP), or both (AP+STA) simultaneously  |
| **Security**           | WPA/WPA2/WPA3 Personal, WEP, and open networks                          |
| **Speed**              | Up to 150 Mbps (theoretical max in 802.11n)                             |
| **IP Stack**           | Built-in TCP/IP stack (lwIP)                                            |
| **Power Management**   | Sleep modes (light, deep sleep) for low power IoT                      |

---

### 🔧 Basic Usage (Arduino Framework)

Here’s a simple example to connect ESP32-WROOM to a Wi-Fi network:

```cpp
#include <WiFi.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
  Serial.begin(115200);

  delay(2000);  // <-- Let the serial port settle

  // Clear screen
  for (int i = 0; i < 20; i++) Serial.println();

  WiFi.begin(ssid, password);

  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Your code here
}
```
---

### 📡 Applications

- IoT home automation
- Sensor data logging to cloud
- Remote device control
- Wi-Fi based camera modules (with ESP32-CAM)
- Web server hosting (ESP32 as local web server)

---

Would you like a sample for **setting up a web server**, using **OTA updates**, or **sending data to an API** using Wi-Fi?
