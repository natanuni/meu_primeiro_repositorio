print("olá mundo")

nome = "Natã"
idade = 34
altura = 1.88

print(nome)
print(idade)
print(altura)

cidade = "Itajaí"
ano_nascimento = 1992

print("sou", nome, "moro em", cidade, "nasci no ano ", ano_nascimento)

idade_texto = "33"
idade_numero = int(idade_texto)

print(idade_texto + " anos")
print(idade_numero + 1)

altura = str(1.88)
print("Altura: " + altura + "m")

print(28, 12, 1992)
# O sep="" ele define o que vai estar entre os espaços de cada variável
print(28, 12, 1992, sep="/")
# O end=" " define que a proxima linha continue sem quebrar como de padrão
print(28, 12, 1992, end=" ")
print("Meu aniversário")
print("teste")

# aprendendo input()
nome_1 = input("qual é o nome? ")
print("Prazer conhecer você, ", nome_1)

texto_idade = input("qual é a sua idade? ")
numero_idade = int(texto_idade)
print("Ano que vem você terá ", numero_idade + 1, " anos")

# Calculando preço de desconto
preco = 70
# 20% de desconto
desconto = 0.20

preco_final = preco - (preco * desconto)
print(preco_final)

# Operações
minutos_totais = 120
horas =  minutos_totais // 60
minutos_restantes = minutos_totais % 60

print(horas, "h", minutos_restantes, "min")

valor_compra = float(input("Digite o Valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))
valor_troco = valor_pago - valor_compra
nota_10 = valor_troco // 10
moeda_1 = valor_troco % 10

print("Uma camiseta no preço ", valor_compra, "Fábio pagou ", valor_pago, "contente com a compra foi conferir o troco e viu ", nota_10, " notas e ", moeda_1, " de moedas")
