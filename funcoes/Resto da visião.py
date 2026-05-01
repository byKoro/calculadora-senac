def Resto_de_divisao():
    while True:
        print("Resto de divisão: ")
        print("Digite 0 se quiser sair")
        n1 = float(input("Digite o Numero"))
        n2 = float(input("Digite o Numero"))
        if n1 == 0 :
            print("Voltando")
            break
        elif n1 <0 or n2 <0:
            print("Error!")
        else:
            resto = n1 % n2
            print(f"Resto da divisao: {resto}")
            break
Resto_de_divisao()