while True:
    try:
        Numero = int(input("Digite um numero: "))
        break
    except ValueError:
        print("Entrada invalida! Digite um numero, não uma letra.")
