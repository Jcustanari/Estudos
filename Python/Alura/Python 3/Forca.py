
def Jogar():
   
    print("#####################################")
    print("#####Bem vindo ao jogo de Forca!#####")
    print("#####################################\n")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False
    letras_acertadas = ["_","_","_","_","_","_",]
    
    print(letras_acertadas)
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim do jogo!")

if(__name__ == "__main__"):
    Jogar()