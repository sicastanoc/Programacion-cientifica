import serial
import pyautogui 

# Configura los parámetros de la comunicación serial
port = "COM7"          # Reemplaza con el nombre de tu puerto COM
baudrate = 115200
data_bits = 8
parity = serial.PARITY_NONE
stop_bits = 1

while True:

    try:
        # Abre la conexión serial
        ser = serial.Serial(port, baudrate, data_bits, parity, stop_bits)

        # Lee datos del dispositivo
        received_data = ser.readline().decode('utf-8').strip()
        if received_data == '1':
            pyautogui.press('volumeup')
        if received_data == '2':
            pyautogui.press('volumedown')
        if received_data == '3':
            pyautogui.press('playpause')
        print(f"Recibido: {received_data}")



    except serial.SerialException as e:
        print(f"Error de comunicación serial: {e}")

    finally:
        # Cierra la conexión serial al finalizar
        if ser.is_open:
            ser.close()
