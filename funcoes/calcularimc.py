def imc_pessoa(peso, altura):
    return peso / (altura * altura)

peso = float(input("Digite seu peso corporal: "))
altura = float(input("Digite sua altura: "))

resultado = imc_pessoa(peso, altura)

if resultado < 18.5:
    print(f"Seu IMC é de {resultado:.2f}  Abaixo do peso!")
elif resultado >= 18.5 and resultado <= 24.9:
    print(f"Seu IMC é de {resultado:.2f}  Peso ideal!")
elif resultado >= 25 and resultado <= 29.9:
    print(f"Seu IMC é de {resultado:.2f}  Sobrepeso!")
elif resultado > 30:
    print(f"Seu IMC é de {resultado:.2f}  Obesidade!")