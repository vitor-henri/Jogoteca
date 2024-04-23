import random

frutas = open('forca/lista_frutas.txt','r',encoding='utf8')
fruta = frutas.read()
lista_frutas = fruta.split("\n")

animais = open('forca/lista_animais.txt','r',encoding='utf8')
animal = animais.read()
lista_animais = animal.split("\n")

objetos = open('forca/lista_objetos.txt','r',encoding='utf8')
objeto = objetos.read()
lista_objetos = objeto.split("\n")

def escolhe_tema():
    print('1. Frutas')
    print('2. Animais')
    print('3. Objetos\n')
    escolha = (input('Escolha o tema: '))
    if escolha == "1":
        print("O tema é frutas!")
        return lista_frutas
    if escolha == "2":
        print("O tema é animais!")
        return lista_animais
    if escolha == "3":
        print("O tema é objetos!")
        return lista_objetos

def escolhe_palavra(lista:list):
    palavra_escolhida = random.choice(lista)
    return palavra_escolhida

def vidas(palavra:str):
    vida = len(palavra)
    if vida <=3:
        chances = 8
        return chances
    if vida > 3 and vida <= 5:
        chances = 10
        return chances
    if vida >5 and vida <= 7:
        chances = 13
        return chances
    if vida >7:
        chances = 15
        return chances

def cria_mascara(palavra:str):
    letras = len(palavra)
    mascara=[]
    for numeros in range(letras):
        mascara.append("_")
    return mascara   

def preenche_mascara(palavra:str,letra:str,lista:list):
    mascara = lista

    contador = 0
    chute = letra
    if chute == palavra:
        print('Voce ganhou')
    for letras in palavra:
        if chute == letras:
            mascara[contador] = chute
        contador += 1

    contador = 0

    return mascara

def vitoria(palavra:str,letra:str,lista:list):
    if "_" not in lista:
        print('Voce ganhou!')
        print(f'A palavra era {palavra}')
        exit()
    if palavra == letra:
        print('Voce ganhou!')
        print(f'A palavra era {palavra}')
        exit()