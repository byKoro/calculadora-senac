def cateto():
    hipotenusa = int(input("Digite o valor da hipotenusa: "))
    cateto_a = int(input("Digite o valor do cateto: "))

    if hipotenusa < cateto_a:
        print("Hipotenusa não pode ser menor que o cateto!")
    else:
        calculo_cateto = (hipotenusa ** 2 - cateto_a ** 2) ** 0.5

    print(f"Valor do cateto: {calculo_cateto:.2f}")