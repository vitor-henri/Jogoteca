from forca.jogo_da_forca import *
import os
import time
def jogo_forca():
    os.system('cls')

    escolha = escolhe_tema()
    palavra_secreta = escolhe_palavra(escolha)

    mascara = cria_mascara(palavra_secreta)

    chances = vidas(palavra_secreta)

    chutes = []

    while chances > 0:

        print(f"Você tem {chances} vidas")
        print(*mascara)
        chute = str(input('Chute:')).upper()
        chutes.append(chute)
        print(chutes)
        preenche = preenche_mascara(palavra_secreta,chute,mascara)    
        print()
        if chute in palavra_secreta:
            pass
        if chute not in palavra_secreta:
            chances -= 1
        vitoria(palavra_secreta,chute,mascara)
        time.sleep(1)
        os.system('cls')
    os.system('cls')
    vitoria(palavra_secreta,chute,mascara)

if __name__ == "__main__":
    jogo_forca()