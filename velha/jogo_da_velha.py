import os

tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]

marcador = "X"

vencedor = False

jogadas = 1

def mostrarTabuleiro():
    print(f" {tabuleiro[0]} │  {tabuleiro[1]}  │ {tabuleiro[2]}")
    print("───┼─────┼───")
    print(f" {tabuleiro[3]} │  {tabuleiro[4]}  │ {tabuleiro[5]}")
    print("───┼─────┼───")
    print(f" {tabuleiro[6]} │  {tabuleiro[7]}  │ {tabuleiro[8]}")

while True:
    os.system("cls")

    print("\033[34m\033[1m*Jogo da Velha*\033[0;0m\nOs espaços vazios são marcados com o número referente a sua posição.\n")

    #Tabuleiro
    mostrarTabuleiro()

    #Execução
    print(f'\n\033[35m*Jogador {marcador}*\033[0;0m')
    posicao = int(input("Em qual posição você quer jogar? "))

    if posicao > 9 or posicao < 1 or type(tabuleiro[posicao-1]) != int:

        input("*Escolha outra posição (Aperte para continuar)*")

    else:

        tabuleiro[posicao-1] = marcador

        for i in range(3):

            #Horizontal
            if tabuleiro[i*3] == tabuleiro[i*3+1] and tabuleiro[i*3]  == tabuleiro[i*3+2]:
                vencedor = True
            
            #Vertical
            elif tabuleiro[i] == tabuleiro[i+3] and tabuleiro[i] == tabuleiro[i+6]:
                vencedor = True

        if tabuleiro[0] == tabuleiro[4] and tabuleiro[0] == tabuleiro[8] or tabuleiro[2] == tabuleiro[4] and tabuleiro[2] == tabuleiro[6]:
            vencedor = True

        if vencedor:
            os.system("cls")
            mostrarTabuleiro()
            print(f"\n*Parabéns, Jogador \033[33m<(.xX_$[\033[35m{marcador}\033[33m]$_Xx.)>\033[0;0m vencedor o Jogo da Velha*")
            break
        elif jogadas == 9:
            os.system("cls")
            mostrarTabuleiro()
            print("\n*Os jogadores empataram, \033[31mNENHUM GANHADOR!\033[0;0m*")

        marcador = "X" if marcador == "O" else "O"
