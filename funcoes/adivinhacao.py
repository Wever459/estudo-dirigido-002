def jogo_adivinha():
    segredo = 7
    tentativas = 0

    while True:
        try:
            chute = int(input("Adivinha o número (0-10): "))
        except ValueError:
            print("Digite apenas números!")
            continue

        tentativas += 1

        if chute == segredo:
            print("Acertou!")
            break
        elif chute < segredo:
            print("Muito baixo!")
        else:
            print("Muito alto!")

jogo_adivinha()