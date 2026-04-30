def somar():
  print("-=-=-==-Somar-=-=-==-")
  while True:
    somar = 0
    print("Digíte 0 para voltar")
    while True:
      n1 = int(input("Digíte um número para somar: "))
      if n1 == 0:
        print("<-")
        break
      somar += n1
      print(f"Resultado: {somar}")
    break