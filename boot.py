import machine
import time
from machine import UART

# Configura el pin 27 como una entrada con pull-up
button_pin_1 = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin_2 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin_3 = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_UP)
button_pin_4 = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)

# Configura la comunicación UART (ajusta los pines y la velocidad según tu configuración)
uart = UART(0, baudrate = 115200)
uart.init( baudrate=115200, bits = 8, parity = None, stop=1)  # UART1, pines 17 (TX) y 16 (RX)

# Configura el pin 13 como una salida
led_pin = machine.Pin(13, machine.Pin.OUT)

while True:
    # Verifica si el botón está presionado (debido a la resistencia pull-up)
    if not button_pin_1.value():
        mensaje = "1\n"
        uart.write(mensaje)
        time.sleep_ms(500) 
    if not button_pin_2.value():
        mensaje = "2\n"
        uart.write(mensaje)
        time.sleep_ms(500) 
    if not button_pin_3.value():
        mensaje = "3\n"
        uart.write(mensaje)
        time.sleep_ms(500) 
    if not button_pin_4.value():
        mensaje = "4\n"
        uart.write(mensaje)
        time.sleep_ms(500) 
