
print("#####################################")
print("Bem vindo ao jogo de Adivinhação!")
print("#####################################\n")

numero_secreto = 42
tentativas = 3
rodadas = 1

while (rodadas <= tentativas):
    print("Tentativas {} de {}".format(rodadas,tentativas))
    chute = int(input("Digite um numero: "))
    print("\n")

    if (numero_secreto == chute):
        print("Voce acertou!!!")
    else:
        if(chute > numero_secreto):
            print("Voce Errou! o seu chute foi maior que o numero secreto")
        elif(chute < numero_secreto):
            print("Voce Errou! o seu chute foi menor que o numero secreto")
    rodadas = rodadas + 1

print("Fim do Jogo!")