def moda():
  numeros = input("Digite os números separados por vírgula: ")
  numeros = [float(num.strip()) for num in numeros.split(",")]
  
  frequencia = {}
  for num in numeros:
    if num in frequencia:
      frequencia[num] += 1
    else:
      frequencia[num] = 1
  
  moda = max(frequencia, key=frequencia.get)
  
  print(f"A moda é: {moda}")
  