print("Resto de divisão: ")
while True:
    sair = 0
    print("Digite 0 se quiser sair")
        
    n1 = int(input("Digite o Numero"))
    n2 = int(input("Digite o Numero"))
    if n1 == 0 :
        print("Voltando")
        break
    elif n1 <0 or n2 <0:
        print("Error!")
    else:
        soma = n1 % n2
        print(f"Resto da divisao: {soma}")
    