import math

def calcular_area_triangulo():
    print("=========Área do Triângulo=========")
    
    while True:
        print("Escolha a fórmula para calcular a área do triângulo:")
        print("1 -  Base e Altura")
        print("2 -  3 lados (Fórmula de Heron)")
        print("3 -  Dois Lados + 1 Ângulo (Fórmula de Seno)")
        print("4 - Sair")

        op = int(input("Opção: "))
        if op == 1:
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            area = (base * altura) / 2
            print(f"A área do triângulo é: {area:.2f}")
            novamente = input("Calcular novamente? (s/n): ").strip().lower()
            if novamente != 's':
                break

        elif op == 2:
            a = float(input("Digite o lado a: "))
            b = float(input("Digite o lado b: "))
            c = float(input("Digite o lado c: "))
            if a + b <= c or a + c <= b or b + c <= a:
                print("Esses lados não formam um triângulo válido.")
                continue
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"A área do triângulo é: {area:.2f}")
            novamente = input("Calcular novamente? (s/n): ").strip().lower()
            if novamente != 's':
                break

        elif op == 3:
            lado1 = float(input("Digite o primeiro lado: "))
            lado2 = float(input("Digite o segundo lado: "))
            angulo = float(input("Digite o ângulo entre os lados (em graus): "))
            area = (lado1 * lado2 * math.sin(math.radians(angulo))) / 2
            print(f"A área do triângulo é: {area:.2f}")
            novamente = input("Calcular novamente? (s/n): ").strip().lower()
            if novamente != 's':
                break

        elif op == 4:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")