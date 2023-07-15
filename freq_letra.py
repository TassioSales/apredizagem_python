# Criar um programa que conte a frequência de cada letra em uma string.
def freq_letra(string):
    frequencia = {}
    for letra in string:
        frequencia[letra] = frequencia.get(letra, 0) + 1
    return frequencia


def main():
    string = input("Digite uma string: ")
    frequencia = freq_letra(string)
    print(frequencia)


if __name__ == '__main__':
    main()
