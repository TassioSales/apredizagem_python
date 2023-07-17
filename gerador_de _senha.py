import random
import string
import os
import locale

class GeradorSenha:
    def __init__(self):
        self.letras = string.ascii_letters
        self.numeros = string.digits
        self.caracteres_especiais = string.punctuation.replace('"', '').replace("'", "")

    def gerar_senha(self, comprimento, qtd_letras, qtd_numeros, qtd_caracteres_especiais):
        caracteres_permitidos = ''
        senha = ''

        total_caracteres = qtd_letras + qtd_numeros + qtd_caracteres_especiais

        if total_caracteres > comprimento:
            raise ValueError("A soma das quantidades de letras, números e caracteres especiais deve ser menor ou igual ao comprimento da senha.")

        if qtd_letras > 0:
            caracteres_permitidos += self.letras
            senha += ''.join(random.choice(self.letras) for _ in range(qtd_letras))

        if qtd_numeros > 0:
            caracteres_permitidos += self.numeros
            senha += ''.join(random.choice(self.numeros) for _ in range(qtd_numeros))

        if qtd_caracteres_especiais > 0:
            caracteres_permitidos += self.caracteres_especiais
            senha += ''.join(random.choice(self.caracteres_especiais) for _ in range(qtd_caracteres_especiais))

        complemento = comprimento - len(senha)
        senha += ''.join(random.choice(caracteres_permitidos) for _ in range(complemento))

        senha = ''.join(random.sample(senha, len(senha)))
        return senha

    def verificar_senha_arquivo(self, senha, pasta_documentos):
        nome_arquivo = os.path.join(pasta_documentos, "senhas.txt")

        try:
            with open(nome_arquivo, "r") as arquivo:
                senhas_salvas = arquivo.readlines()
                for senha_salva in senhas_salvas:
                    if senha == senha_salva.strip():
                        return True
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

        return False

    def salvar_senha_arquivo(self, senha, pasta_documentos):
        if self.verificar_senha_arquivo(senha, pasta_documentos):
            print("A senha gerada já foi usada anteriormente. Por favor, gere uma nova senha.")
            return

        nome_arquivo = os.path.join(pasta_documentos, "senhas.txt")

        try:
            with open(nome_arquivo, "a") as arquivo:
                arquivo.write(senha + "\n")
            print(f"A senha foi salva com sucesso no arquivo {nome_arquivo}.")
        except Exception as e:
            print(f"Erro ao salvar a senha no arquivo: {e}")

if __name__ == "__main__":
    gerador = GeradorSenha()

    comprimento_senha = int(input("Digite o comprimento total da senha desejado: "))
    qtd_letras = int(input(f"Digite a quantidade de letras desejada na senha (faltam {comprimento_senha} caracteres): "))
    qtd_numeros = int(input(f"Digite a quantidade de números desejada na senha (faltam {comprimento_senha - qtd_letras} caracteres): "))
    qtd_caracteres_especiais = int(input(f"Digite a quantidade de caracteres especiais desejados na senha (faltam {comprimento_senha - qtd_letras - qtd_numeros} caracteres): "))

    senha_gerada = gerador.gerar_senha(comprimento_senha, qtd_letras, qtd_numeros, qtd_caracteres_especiais)
    print("Senha gerada:", senha_gerada)

    # Obter pasta de documentos de acordo com o idioma do sistema
    idioma_sistema = locale.getdefaultlocale()[0]

    if idioma_sistema.startswith("pt"):
        nome_pasta_documentos = "Documentos"
    else:
        nome_pasta_documentos = "Documents"

    diretorio_pasta_documentos = os.path.join(os.path.expanduser("~"), nome_pasta_documentos)

    # Verifica se o diretório da pasta de documentos existe antes de salvar
    if not os.path.exists(diretorio_pasta_documentos):
        os.makedirs(diretorio_pasta_documentos)

    gerador.salvar_senha_arquivo(senha_gerada, diretorio_pasta_documentos)
