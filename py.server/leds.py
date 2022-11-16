# leds.py "tamanho da seq"

import sys
import serial
import time
import string
import random

# make sure the 'COM#' is set according the Windows Device Manager
tamanho = sys.argv[1]
tamanho = int(tamanho)
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)
cores = 'rgby'

for i in range(tamanho):
    cor = random.choice(cores)
    resposta = 'x'
    ser.write(cor.encode())
    
    while resposta != 'k':
        resposta = ser.read()
        resposta = str(resposta, encoding='utf-8')
        
    resposta = 'x'
    while resposta != 'd':
        resposta = ser.read()
        resposta = str(resposta, encoding='utf-8')

ser.close()