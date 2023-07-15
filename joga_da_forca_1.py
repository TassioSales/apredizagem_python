import random


def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "linguagem", "internet"]
    return random.choice(palavras)


def exibir_forca(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()


def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas_maximas = 6
    tentativas = tentativas_maximas
    pontuacao = 0

    print("Bem-vindo ao Jogo da Forca!")
    exibir_forca(palavra_secreta, letras_corretas)

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra válida.")
            continue

        if letra in letras_corretas:
            print("Você já tentou essa letra antes.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            pontuacao += 1
        else:
            tentativas -= 1
            print(f"A letra '{letra}' não faz parte da palavra. Tentativas restantes: {tentativas}")

        exibir_forca(palavra_secreta, letras_corretas)

        if all(letra in letras_corretas for letra in palavra_secreta):
            print("Parabéns! Você acertou a palavra!")
            break

    else:
        print(f"Fim de jogo! A palavra secreta era: '{palavra_secreta}'.")

    pontuacao_final = pontuacao * tentativas
    print(f"Pontuação final: {pontuacao_final}")


if __name__ == "__main__":
    jogar_forca()
