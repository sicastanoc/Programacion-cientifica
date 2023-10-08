import machine
import time

# Configura el pin 27 como una entrada con pull-up
button_pin = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

# Configura el pin 13 como una salida
led_pin = machine.Pin(13, machine.Pin.OUT)

while True:
    # Verifica si el botón está presionado (debido a la resistencia pull-up)
    if not button_pin.value():
        print("Se presiono el boton")
        # Cambia el estado del pin 13 (enciende/apaga el LED)
        led_pin.value(not led_pin.value())
        # Espera un tiempo breve para evitar el rebote del botón
        time.sleep_ms(200)

