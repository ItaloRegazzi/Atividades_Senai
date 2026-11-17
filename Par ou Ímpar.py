while True:
    numero:int = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
    continuar = input("Deseja verificar outro número? (s/n): ")
    if continuar.lower() != "s":
        break
    numero = int(input("Digite um número inteiro: "))
    continue