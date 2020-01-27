
print("#####################################")
print("Bem vindo ao jogo de Adivinhação!")
print("#####################################\n")

numero_secreto = 42
tentativas = 3


for rodadas in range(0,tentativas,1):
    print(f"Tentativas {rodadas+1} de {tentativas}") #.format(rodadas+1,tentativas))
    chute = int(input("Digite um numero entre 1 e 100: "))
    print("\n")

    if (chute < 1 or chute > 100):
        print("Valor digitado tem que estar entre 1 e 100!")
        continue
    if (numero_secreto == chute):
        print("Voce acertou!!!")
        break
    else:
        if(chute > numero_secreto):
            print("Voce Errou! o seu chute foi maior que o numero secreto")
        elif(chute < numero_secreto):
            print("Voce Errou! o seu chute foi menor que o numero secreto")
    rodadas = rodadas + 1

print("Fim do Jogo!")