# Todas as funções devem ser colocadas no arquivo __init__.py
import funcoes

# Para inserir sua funcionalidade nova, apenas coloque o nome dela na chave e importe a função para o valor, sem os paranteses.abs

funcoes = {
  "Somar": funcoes.somar,
  "Multiplicar": funcoes.multiplicar,
  "Subtrair Dois Números": funcoes.subtrair
  # "Subtrair": funcoes.subtrair
}

# Não mexer daqui pra baixo, está funcionando!

def menu_calculadora():
  while True: 
    n = 1
    opcoes = ["0"]
    for nome in funcoes:
      print(f"{n}.{nome}")
      opcoes.append(n)
      n += 1
    print("0.Fechar o programa")

    escolha = input("Escolha uma opção: ")
    while escolha not in str(opcoes):
      print("Opção inválida: ")
      escolha = input("Escolha uma opção: ")
    escolha = int(escolha)
    if escolha == 0:
      print("Programa finalizado!")
      break
    
    nomes = list(funcoes.keys())
    funcao_escolhida = funcoes[nomes[escolha - 1]]
    funcao_escolhida()

menu_calculadora()