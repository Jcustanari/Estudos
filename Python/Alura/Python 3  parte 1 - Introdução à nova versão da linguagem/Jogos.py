
import Adivinhacao
import Forca

def escolha_jogo():
    print("#####################################")
    print("########## Escolha o jogo! ##########")
    print("#####################################\n")

    while(1):
        jogo = int(input("(1) Forca (2) Adivinhação"))

        if(jogo == 1):
            print("Jogando forca!1")
            Forca.Jogar()
            break
        elif(jogo == 2):
            print("Jogando advinhação!")
            Adivinhacao.Jogar()
            break
        else:
            print("Opção invalida! tente novamente!\n")

if(__name__ == "__main__"):
    escolha_jogo()