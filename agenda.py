contatos = []

def adicionar (nome, telefone):
    contatos.append({"nome": nome, "telefone": telefone})

adicionar("Gilmar", "47 9711-1636")
adicionar("Maykon", "47 992674162")
adicionar("Natã", "47 999206729")

for contato in contatos:
    print(contato["nome"], "-", contato["telefone"])