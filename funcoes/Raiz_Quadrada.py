import math
def Raiz_Quadrada():
    while True:
        try:
            numero = int(input("Informe o numero: "))
            break
        except ValueError:
            print("Erro: digite apenas números inteiros.")
            
    if numero < 0:
        print("Erro: não é possível calcular raiz de número negativo.")
        return
    
    print(f"{math.sqrt(numero):.2f}")