# buttons.py

import sys
import serial
import time
import string
import random

# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)
sequencia_real = sys.argv[1]
sequencia_lida = ""

for i in range(5):
    ser.write('p'.encode())
    
    resposta = ''
    while resposta != 'k':
        resposta = ser.read()
        
    resposta = ''
    while resposta != 'r' and resposta != 'g' and resposta != 'b' and resposta != 'y' and resposta != 'n':
        resposta = ser.read()
    
    sequencia_lida = sequencia_lida + resposta
#print(sequencia_real)
print(sequencia_lida)
#print(sequencia_lida == sequencia_real)
ser.close()