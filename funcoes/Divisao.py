# Operação Aritimetica de Divisão 

def divisao():

    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            resultado = numero1 / numero2

            print("Resultado da divisão:", resultado)
            break

        except ValueError:
            print("Erro: Digite somente números.")

        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero.")

divisao()

