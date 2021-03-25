#RafaelMatos
#rafaelmatosrv@gmail.com
#Usar ordem OCO

import time

from PIL import ImageGrab
import pyautogui

X1 = 1200    #Coordenada x da barra que será lida no histograma
Y1 = 550     #Coordenada x da barra que será lida no histograma


def capture_screen():  #Funcao de captura de tela
    screen = ImageGrab.grab()
    return screen


def detect_Venda(screen):
    color = screen.getpixel((X1, Y1))
    if color == (0, 0, 0)   : #Verifica se a com é Preta
        return True

def detect_Compra(screen):
    color = screen.getpixel((X1, Y1))
    if color == (255, 255, 255)   :    #Verifica se a com é Branca
        return True


def Venda():

    pyautogui.click(1790, 581)    #Coordenada x e y do botao venda a mercado
    time.sleep(120)# Tempo para proxima leitura 120 segundos

def Compra():

    pyautogui.click(1620, 581)  #Coordenada x e y do botao venda a mercado
    time.sleep(120) # Tempo para proxima leitura 120 segundos



while True:
    screen = capture_screen()
    if detect_Venda(screen):
        Venda()
    elif detect_Compra(screen):
        Compra()
