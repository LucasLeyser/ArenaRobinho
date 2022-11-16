# buttons.py
import sys
import serial
import time
import string
import random

def buttons():

    # make sure the 'COM#' is set according the Windows Device Manager
    ser = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)

    ser.write('p'.encode())

    resposta = 'x'
    while resposta != 'k':
        resposta = ser.read()
        resposta = str(resposta, encoding='utf-8')
        
    resposta = 'x'
    while resposta != 'r' and resposta != 'g' and resposta != 'b' and resposta != 'y' and resposta != 'n':
        resposta = ser.read()
        resposta = str(resposta, encoding='utf-8')
        
    ser.close()
    return resposta

retorno = buttons()
print (retorno)
