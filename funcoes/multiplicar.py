
def multiplicar():
    print("=-=-=-=-Multiplicar-=-=-=-=")

    while True:
        
        n1= float(input("Digite o primeiro número: "))

        n2= float(input("Digite o segundo número: "))

        resultado = n1 * n2

        print(f"Resultado: {resultado}")
        
        continuar = input("Deseja realizar outra multiplicação? (s/n): ").lower()

        if continuar != 's':
            print("Voltando ao menu principal...")
            break
  