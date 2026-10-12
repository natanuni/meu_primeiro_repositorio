def medias(nota):
    return nota / 2

print(medias(8.0))

def desconto(preco, percentual=10):
    return preco - preco * percentual / 100

print(desconto(200))
print(desconto(200, 50))

def estatisticas(notas):
    return max(notas), min(notas), sum(notas) / len(notas)

maior, menor, media = estatisticas ([7.0, 9.5, 6.5])
print(maior, menor, round(media, 1))