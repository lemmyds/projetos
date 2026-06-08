import time

while True:
    tentativas = 3
    while tentativas > 0:
        palavra = input("Digite a palavra: ")
        if palavra == "matheus":
            print("Acertou!")
            break
        tentativas -= 1
        print(f"Errado! Tentativas restantes: {tentativas}")

    if tentativas > 0:
        break  # acertou, sai totalmente
    print("Fim - você errou 3 vezes! Reiniciando...")
    time.sleep(1)

