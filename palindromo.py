def palindromo(texto):
    if texto == texto[::-1]:
        print(f"{palavra} é um palindromo.")
    else:
        print(f"{palavra} não é um palindromo.")


if __name__ == '__main__':

    palavras = [
        "ana", "arara", "radar", "reger", "asa", "natan", "puxar",
        "sobrevivente", "osso", "reviver", "reler", "reter",
        "matam", "mirim", "reconocer", "deleveled", "refer",
        "sopapos", "esse", "mussum", "omissíssimo", "python",
        "programação", "computador", "internet", "linguagem",
        "modelo", "treinamento", "desenvolvimento"
    ]

    for palavra in palavras:
        palindromo(palavra)
