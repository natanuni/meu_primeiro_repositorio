# Comparar valores para tomar decisões
nota_joao = 7.5
nota_maria = 6.2

# maior
comparacao_joao = nota_joao >= 7
comparacao_maria = nota_maria >= 7
print("maior ", comparacao_joao, comparacao_maria)
# menor
comparacao_joao_2 = nota_joao <= 7
comparacao_maria_2 = nota_maria <=7
print("menor ", comparacao_joao_2, comparacao_maria_2)
# igual
comparacao_joao_3 = nota_joao == 7
comparacao_maria_3 = nota_maria == 7
print("igual ", comparacao_joao_3, comparacao_maria_3)
# diferente
comparacao_joao_4 = nota_joao != 7
comparacao_maria_4 = nota_maria != 7
print("diferente ", comparacao_joao_4, comparacao_maria_4)

# função bool categoriza o vizivel semdo texto ou numeor não sendo 0
print("Testando a função bool")
print(bool(0))
print(bool(33))
print(bool(""))
print(bool("zero")) 

# exemplo do slide
renda = float(input("Renda mensal: "))
score = int(input("Score de crédito (0-1000): "))

renda_aprovado = renda >= 3000 and score >= 600
print("Empréstimo aprovado?", renda_aprovado)

# atividade
nota_atual = float(input("Digite a nota: "))
frequencia = int(input("Digite a frequencia: "))

aluno_aprovado = nota_atual >= 7 and frequencia >= 75
print("Maykon esta aprovado: ", aluno_aprovado)

aluno_recupera = not aluno_aprovado
print("Maykon precisa de recuperação: ", aluno_recupera)

if nota_atual >= 7:
    print("aprovado")
elif nota_atual >=6:
    print("recuperação")
else:
    print("reprovado")

# exemplo do slide
for i in range(5):
    print("contando:", i)

number_test = int(input("Digite um número: "))
for n in range(1,11):
    resultado = number_test * n
    print(n, "x", number_test, "=", resultado)