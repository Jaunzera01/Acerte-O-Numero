#Biblioteca:
import random
def gera():
    return random.randint(1,100)

#Jogo, chutes e respostas:
def game():
    resposta = gera()
    tentativa = 10
    print("\nPalpite gerado!")

    chute=10
    while chute is not resposta:
        tentativa +=1
        chute = int(input("Esse foi o seu chute: "))
        if chute > resposta:
            print("Uh! Você errou, o valor é menor que ", chute)
        elif chute < resposta:
            print("Uh! Você errou, o valor é maior que ", chute)
        else:
            print("Parabéns! O número gerado foi ", resposta)
    
while True:
    game()
