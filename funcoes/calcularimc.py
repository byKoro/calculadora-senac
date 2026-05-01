def ler_numero(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except ValueError:
            print("Digite Apenas Numeros!")

def calcularimc():
    print("-=-=-==- Calcular IMC -=-=-=-=")
    
    while True:
        print("Digite 0 para voltar")

        peso = ler_numero("Digite seu peso corporal: ")
        if peso == 0:
            print("<-")
            break

        altura = ler_numero("Digite sua altura: ")
        if altura == 0:
            print("<-")
            break

        resultado = peso / (altura * altura)

        if resultado < 18.5:
            print(f"Seu IMC e de {resultado:.2f} - Abaixo do peso.")
        elif resultado <= 24.9:
            print(f"Seu IMC e de {resultado:.2f} - Peso ideal.")
        elif resultado <= 29.9:
            print(f"Seu IMC e de {resultado:.2f} - Sobrepeso.")
        else:
            print(f"Seu IMC e de {resultado:.2f} - Obesidade.")

        print("-" * 30)