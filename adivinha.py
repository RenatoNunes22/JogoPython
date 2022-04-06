import random

def jogar_adivinha():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101))
    total_tentativas = 0

    pontos = 1000
    print("Qual nivel de dificuldade ?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas + 1):
        print("Tentativa {} de {} ". format(rodada, total_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou")
            break;
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")

            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos -= pontos_perdidos
        rodada += 1

    print("Fim do jogo")
    print("Numero secreto é: {}" .format(numero_secreto))
    print("Sua pontuacao foi: {}".format(pontos))

if(__name__ == "__main__"):
    jogar_adivinha()
