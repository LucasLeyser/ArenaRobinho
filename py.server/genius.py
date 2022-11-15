# genius.py

import serial
import time
import string
import random

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)
cores = 'rgby'

for i in range(5):
    cor = random.choice(cores)
    #print(cor)
    ser.write(cor.encode())
    
    resposta = ' '
    while resposta != 'k':
        resposta = ser.read()
        
    resposta = ' '
    while resposta != 'd':
        resposta = ser.read()

ser.close()