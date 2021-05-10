desvio padrão,label={Media_DP}]
import math

def media(path):
    pega_valor = open(path,'r')            #abre aquivo indicado no caminho
    n = input()                            #numero de amostras
    x3 = 0
    for i in range(n):
        x1 = float(pega_valor.readline())
        x2 = float(pega_valor.readline())
        x3 += x2-x1

    media = x3 / n
    pega_valor.close()                     #fecha arquivo
    return media

def desvio_padrao(path,media):
    pega_valor = open(path, 'r')           # abre aquivo           
    x3 = 0
    x4 = 0
    for i in range(n):
        x1 = float(pega_valor.readline())
        x2 = float(pega_valor.readline())
        x3 = x2 - x1
        x4 += (x3 - media)**2              #soma os desvios

    desvio  = (x4 / n)**(0.5)              #desvio padrão
    pega_valor.close()                     # fecha arquivo
    return desvio


path = '/home/gustavo/note.txt'
r = media(path)
print(r)
print(desvio_padrao(path,r))
