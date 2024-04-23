# Dev From Vito
from adivinhacao.jogo_da_adivinhacao import *
from forca.jogo_da_forca import *
import time

print("  Bem-Vindo a jogoteca do vito  \n")
time.sleep(1)

# Veificando idade para poder jogar e mandando o menu
idade_do_menino = int(input("Qual sua idade para poder iniciar a jogoteca? "))
if idade_do_menino >= 18:
    jogo = input("""\t(Menu Principal)\n
    (Escolha um Número para entrar no jogo)
    1- Jogo da Velha pau no cu
    2- Jogo da Adivinhação fdpta
    3- Jogo da forca se mata
    4- Calculadora Mortifera
    Digite sua resposta: """)
else:
    print("Sai daq mlk do kraio o bglh é pra de maior")
    exit

# chamando o jogo da forca
if jogo == 2:
    adivinhacao()

# chamando o jogo da forca
elif jogo == 3:
    pass