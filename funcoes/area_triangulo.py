import math

def calcular_area_triangulo(a, b, c):
    # Verificar se os lados são positivos
    if a <= 0 or b <= 0 or c <= 0:
        return "Erro: os lados devem ser positivos."
    
    # Verificar a desigualdade triangular
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Erro: esses lados não formam um triângulo válido."
    
    # Fórmula de Heron
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area