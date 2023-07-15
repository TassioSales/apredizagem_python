# Desenvolver uma função que encontre a soma dos dígitos de um número inteiro.
def somar_digitos(numero):
    soma = 0
    while numero > 0:
        soma = soma + numero % 10
        numero = numero // 10
    return soma


def main():
    numero = int(input("Digite um número: "))
    print(somar_digitos(numero))


if __name__ == '__main__':
    main()
