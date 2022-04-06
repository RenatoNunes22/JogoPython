import forca
import adivinha

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("jogo da foca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("jogo de advinhacao")
        adivinha.jogar_adivinha()

if(__name__ == "__main__"):
    escolher_jogo()
