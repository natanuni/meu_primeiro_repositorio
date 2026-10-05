with open("diario.txt", "w", encoding="utf-8") as diario:
    diario.write("Criando um arquivo txt de um diario\n")
    diario.write("Depois eu tenho que acrescentar mais informações\n")
    diario.write("Hoje pode ser que vá chover\n")
with open("diario.txt", "a", encoding="utf-8") as diario:
    diario.write("Espero que não chova a noite toda\n")
    diario.write("Amanhã a terra vai ficar enxarcada\n")
    diario.write(input("digite um texto: "))
with open("diario.txt", "r", encoding="utf-8") as diario:
        for linha in diario:
          print(linha.strip())