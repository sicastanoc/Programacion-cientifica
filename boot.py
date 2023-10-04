from machine import Pin
import time

p27 = Pin(27, Pin.IN)
p2 = Pin(2, Pin.OUT)
p2.on()
p13 = Pin(13, Pin.OUT)

estado_led = 0

def setLed(pin):
    global estado_led
    print("Se presiono el boton")
    if estado_led == 0:
        p13.on()
        estado_led = 1
    else:
        p13.off()
        estado_led = 0

    


p27.irq(handler=setLed, trigger=Pin.IRQ_RISING)

while(1):
    p2.on()
    time.sleep_ms(500)
    p2.off()
    time.sleep_ms(500)

