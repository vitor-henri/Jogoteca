import random

#introdução ao jogo.
def adivinhacao():
    print('          BOAS VINDAS!          \n')
    print('          ESSE É O JOGO MORTAL          \n')
    print('          VOCÊ IRÁ PASSAR PELA ADIVINHAÇÃO SUPREMA!          \n')
    print('          ESCOLHA O NIVEL DE DIFICULDADE          \n')
    print('          1 - FACIL = 1 - 5          \n')
    print('          2 - MEDIO = 1 - 20          \n')
    print('          3 - DIFICIL = 1 - 50          \n')
    print('          4 - SENAI = 1 - 100          \n')

    #descobrindo a dificuldade.

    dificuldade_jogo = int(input('          Qual a dificuldade? '))
    tentativas = 1
    if dificuldade_jogo == 1:
        numeros_aleatorios = random.randint(1, 5)
        x = 5
        numero_maximo = 5

    elif dificuldade_jogo == 2:
        numeros_aleatorios = random.randint(1, 20)
        x = 10
        numero_maximo = 20

    elif dificuldade_jogo == 3:
        numeros_aleatorios = random.randint(1, 50)
        x = 20
        numero_maximo = 50

    elif dificuldade_jogo == 4:
        numeros_aleatorios = random.randint (1, 100)
        x = 30
        numero_maximo = 100
    #caso o numero for diferente de 1 2 3 ou 4 entre em loop para perguntar a dificuldade

    if dificuldade_jogo != 1 and dificuldade_jogo != 2 and dificuldade_jogo != 3 and dificuldade_jogo != 4:
        while True:
            dificuldade_jogo= int(input('qual a dificuldade? '))
            if dificuldade_jogo == 1:
                numeros_aleatorios = random.randint(1, 5)
                x = 5
                numero_maximo = 5
                break
            elif dificuldade_jogo == 2:
                numeros_aleatorios = random.randint(1, 20)
                x = 10
                numero_maximo = 20
                break
            elif dificuldade_jogo == 3:
                numeros_aleatorios = random.randint(1, 50)
                x = 20
                numero_maximo = 50
                break
            elif dificuldade_jogo == 4:
                numeros_aleatorios = random.randint (1, 100)
                x = 30
                numero_maximo = 100
                break

    #descobrindo o numero escolhido pelo usuario

    numero = int(input('escolha um numero: '))

    #descobrindo se o numero é igual antes de entrar no loop.

    if numero == numeros_aleatorios:
        print()
        print("Você venceu")
        print()
        print(f'você teve {tentativas} tentativas!')
    elif numero > numero_maximo:
            print(f'era pra ser de 1 a {numero_maximo}')
            print('TENTE NOVAMENTE!')
            tentativas -= 1
    else:
        print()
        print("Tente novamente")
        print()
        print(f'RESTAM {x-tentativas} TENTATIVAS!')
        if numero > numeros_aleatorios:
            print('CHUTE MAIS BAIXO')
        elif numero < numeros_aleatorios:
            print('CHUTE MAIS ALTO')

    #abra o while para descobrir se o numero é igual ao aleatorio!
    while numeros_aleatorios != numero:
        numero = int(input('escolha um numero: '))
        tentativas += 1
    #SE FOR IGUAL, BREAK PARA ENCERRAR O LOOP!
        if numeros_aleatorios == numero:
            print()
            print("Você venceu")
            print()
            print(f'você teve {tentativas} tentativas!')
            break
    #CASO O NUMERO SELECIONADO EXCEDA O MAXIMO, NAO CONTAR TENTATIVAS E MANDAR TENTAR NOVAMENTE.    
        elif numero > numero_maximo:
            print(f'era pra ser de 1 a {numero_maximo}')
            tentativas -= 1
            print('TENTE NOVAMENTE!')

    #SE ATINGIR O LIMITE DE TENTATIVAS, PARE O PROGAMA!
        elif tentativas == x:
            print('')
            print('você excedeu o limite de tentativas.')
            print()
            print("GAME OVER")
            print()
            print(f'a resposta era {numeros_aleatorios}')
            break
    #SE ERRAR, MANDE ELE TENTAR NOVAMENTE!
        else:
            print()
            print("Tente novamente")
            print()
            print(f'RESTAM {x-tentativas} TENTATIVAS!')
            if numero < numeros_aleatorios:
                print('CHUTE MAIS ALTO')
            elif numero > numeros_aleatorios:
                print('CHUTE MAIS BAIXO')

# esse name funciona assim significa que o arquivo so rodara no nome que eu coloquei no caso o main :)
if __name__ == "__main__":
    adivinhacao()