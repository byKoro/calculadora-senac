def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido!")

def subtrair():
    n1 = pedir_numero("Insira o primeiro número: ")
    n2 = pedir_numero("Insira o segundo número: ")
    print("Resultado:", n1 - n2)