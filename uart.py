import machine
import time
from machine import UART

# Configura el pin 27 como una entrada con pull-up
button_pin = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

# Configura la comunicación UART (ajusta los pines y la velocidad según tu configuración)
uart = UART(1, baudrate = 9600)
uart.init(baudrate=9600, bits = 8, parity = None, stop=1)  # UART1, pines 17 (TX) y 16 (RX)

while True:
    if not button_pin.value():
        mensaje = "Estoy vivo\n"
        uart.write(mensaje)
        print("Mensaje enviado: " + mensaje)
        time.sleep(2)  # Espera para evitar enviar múltiples mensajes con una sola pulsación


