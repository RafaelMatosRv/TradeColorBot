#RafaelMatos
#rafaelmatosrv@gmail.com


import time

from PIL import ImageGrab
import pyautogui

X1 = 1200    #Coordenada x da barra que será lida no histograma
Y1 = 550     #Coordenada y da barra que será lida no histograma

#X2= 11
#Y2= 11

#X3= 11
#Y3= 11

flag1 = 0
flag2 = 0

def capture_screen():  #Funcao de captura de tela
    screen = ImageGrab.grab()
    return screen


def detect_Venda(screen):

    color = screen.getpixel((X1, Y1))
    #color2 = screen.getpixel((X2, Y2))
    #color3 = screen.getpixel((X3, Y3))
    if color == (0, 0, 0): #Verifica se a cor da barra é Preta ## and color2(0, 0, 0) and color3(0, 0, 0) ## or color2(0, 0, 0) or color3(0, 0, 0)
        return True


def detect_Compra(screen):
    color = screen.getpixel((X1, Y1))
    #color2 = screen.getpixel((X2, Y2))
    #color3 = screen.getpixel((X3, Y3))
    if color == (255, 255, 255)   :    #Verifica se a cor da barra é Branca## and color2(0, 0, 0) and color3(0, 0, 0) ## or color2(0, 0, 0) or color3(0, 0, 0)
        return True
    
def detect_ResetColor(screen):
    color = screen.getpixel((X1, Y1))
    if color != (0, 0, 0) or color != (255, 255, 255)  :    #Verifica se a cor é diferente de branco ou diferente de preto
        return True

def Venda():

    if (flag1 == 0):
        pyautogui.click(1790, 581)    #Coordenada x e y do botao venda a mercado
        #time.sleep(3600)# Tempo para proxima leitura em segundos

def Compra():

    if (flag2 == 0):
        pyautogui.click(1620, 581)  #Coordenada x e y do botao compra a mercado
        #time.sleep(120) # Tempo para proxima leitura 120 segundos


while True:
    screen = capture_screen()
    if detect_Venda(screen):
        Venda()
        flag1 = 1



    elif detect_Compra(screen):
        Compra()
        flag2 = 1

    elif detect_ResetColor(screen):
        flag1 = 0
        flag2 = 0