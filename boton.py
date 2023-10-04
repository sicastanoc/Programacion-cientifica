from machine import Pin


p27 = Pin(27, Pin.IN)

def setLed(pin):
    print("Se presiono el boton")
    


p27.irq(handler=setLed, trigger=Pin.IRQ_RISING)
