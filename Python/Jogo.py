
print("#####################################")
print("Bem vindo ao jogo de Adivinhação!")
print("#####################################\n")

numero_secreto = 42

chute = int(input("Digite um numero: "))

print("Voce digitou o numero: ", chute)

if (numero_secreto == chute):
    print("Voce acertou!!!")
else:
    print("Voce Errou!!!")

print("Fim do Jogo!")