Numero = -1
while Numero < 0:
    try:
        Numero = int(input("Digite um numero: "))
        if Numero < 0:
            print("Numero invalido! Digite um numero positivo.")
    except ValueError:
        print("Entrada invalida! Digite um numero, não uma letra.")
        Numero = -1 

print(f"Numero cadastrado: {Numero}")
