senha_correta = "python123"
senha = ""

while senha != senha_correta:
  senha = input("digite a senha: ")
  if senha == senha_correta:
    print("acesso liberado")
  else:
    print("senha incorreta. tente novamente")

certo = 3
escolha = ""

while escolha != certo:
  escolha = int(input("escolha um numero de 1 à 10: "))
  if escolha >= 5:
    print("muito alto")
  elif escolha <= 2:
    print("esta perto")
  else:
    print("parabens!!")