To control a **buzzer** using an **ESP32**, you can use a simple GPIO pin to send a signal to the buzzer. Here’s a basic guide using the Arduino IDE:

---

### 🧾 **Requirements**
- ESP32 board
- Active buzzer (or passive if you want to generate tones)
- Jumper wires
- Breadboard (optional)

---

### 🔌 **Wiring**
| Buzzer Pin | Connect To   |
|------------|--------------|
| `+`        | ESP32 GPIO (e.g., GPIO 23) |
| `-`        | GND          |

---

### ✅ **Arduino Code for Active Buzzer**
```cpp
int buzzerPin = 23; // GPIO 23

void setup() {
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  digitalWrite(buzzerPin, HIGH); // Turn buzzer ON
  delay(1000);                   // 1 second
  digitalWrite(buzzerPin, LOW);  // Turn buzzer OFF
  delay(1000);                   // 1 second
}
```

---

### 🎵 **If Using a Passive Buzzer** (for tone control)
```cpp
int buzzerPin = 23;

void setup() {
  // Nothing to do here
}

void loop() {
  tone(buzzerPin, 1000); // Play 1kHz tone
  delay(500);
  noTone(buzzerPin);     // Stop tone
  delay(500);
}
```

---

### ℹ️ **Tips**
- Use an **active buzzer** if you just want ON/OFF beeps.
- Use a **passive buzzer** if you want to play melodies (needs `tone()`).
- You can power the buzzer from 3.3V or 5V, depending on the buzzer type.

Let me know if you're using a **passive buzzer** or want to play a **melody** (like Mario theme 🎮), I can help with that too.