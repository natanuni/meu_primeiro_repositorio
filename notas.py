import csv

with open("notas.csv", newline="", encoding="utf-8") as notas:
    leitor = csv.reader(notas)
    for linha in leitor:
        print(linha)

with open("notas.csv", newline="", encoding="utf-8") as notas:
    for aluno in csv.DictReader(notas):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        print(aluno["aluno"], media)

alunos = [{"aluno": "Maykon", "media": media, "situacao": "aprovado"}, {"aluno": "Natan", "media": media, "situacao": "aprovado"}, {"aluno": "Diego", "media": media, "situacao": "reprovado"}]

with open("medias.csv", "w", newline="", encoding="utf-8") as notas:
    escritor = csv.DictWriter(notas, fieldnames=["aluno", "media", "situacao"])
    escritor.writeheader()
    escritor.writerows(alunos)