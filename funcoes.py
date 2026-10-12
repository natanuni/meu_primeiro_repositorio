def e_bissexto(ano):
    """Retorna True se o ano for bissexto."""
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

print(e_bissexto(2000), e_bissexto(1992))
print(e_bissexto(2022), e_bissexto(2024))