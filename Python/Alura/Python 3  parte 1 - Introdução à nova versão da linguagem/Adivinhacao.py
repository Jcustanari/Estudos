import random

def Jogar():

    print("#####################################")
    print("Bem vindo ao jogo de Adivinhação!")
    print("#####################################\n")

    numero_secreto = round(random.randrange(1,101))
    tentativas = 0
    pontos = 1000

    while(1):
        print("Defina o nivel de jogo!")
        print("(1) Facil (2) Medio (3) Dificil")
        nivel = int(input("Escolha o nivel: "))

        if(nivel == 1):
            tentativas = 20
            break
        elif(nivel == 2):
            tentativas = 10
            break
        elif(nivel == 3):
            tentativas = 5
            break
        else:
            print("Nivel invalido, tente novamente!")
            print("\n")


    for rodadas in range(0,tentativas,1):
        print(f"Tentativas {rodadas+1} de {tentativas}") #.format(rodadas+1,tentativas))
        chute = int(input("Digite um numero entre 1 e 100:"))
        print("\n")

        if (chute < 1 or chute > 100):
            print("Valor digitado tem que estar entre 1 e 100!")
            continue
        if (numero_secreto == chute):
            print(f"Voce acertou e sua pontuação é {pontos}")
            break
        else:
            if(chute > numero_secreto):
                print("Voce Errou! o seu chute foi maior que o numero secreto")
                if (rodadas+1 == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif(chute < numero_secreto):
                print("Voce Errou! o seu chute foi menor que o numero secreto")
                if (rodadas+1 == tentativas):
                        print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))



        rodadas = rodadas + 1
        pontos = pontos - round(abs(numero_secreto - chute))



    print("Fim do Jogo!")

if(__name__ == "__main__"):
    Jogar()