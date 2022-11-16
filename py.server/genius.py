#genius.py "tamamnho da sequencia"
import serial
import time
import string
import random
import sys

def main():
    tamanho = sys.argv[1]
    tamanho = int(tamanho)
    leds = sequencia_leds(tamanho)
    botoes = ""
    
    for i in range(tamanho):
        #robinnho vai até o botão
        botoes = botoes + le_botao()
        
    #print(leds)
    #print(botoes)
    #print(leds == botoes)
    
def sequencia_leds(tam):
    tamanho = tam
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)
    cores = 'rgby'
    sequencia = ""

    for i in range(tamanho):
        cor = random.choice(cores)
        sequencia = sequencia + cor
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
    return sequencia

def le_botao():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
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

#start_time = time.time() 
main()
#print("--- %s seconds ---" % (time.time() - start_time))