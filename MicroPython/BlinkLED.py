import machine

import time

led  = machine.Pin(2, machine.Pin.OUT)


while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

# OR
while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

# OR
while True:
    led.value(True)
    time.sleep(0.5)
    led.value(False)
    time.sleep(0.5)
