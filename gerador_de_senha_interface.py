import random
import string
import os
import locale
import tkinter as tk
from tkinter import ttk
import pyperclip

class GeradorSenha:
    def gerar_senha(self, comprimento, quantidade_letras, quantidade_numeros, quantidade_caracteres):
        letras = string.ascii_letters
        numeros = string.digits
        caracteres_especiais = string.punctuation.replace('"', '').replace("'", "")

        senha = ''

        if comprimento <= 0:
            raise ValueError("O comprimento da senha deve ser maior que zero.")

        if quantidade_letras + quantidade_numeros + quantidade_caracteres != comprimento:
            raise ValueError("A soma das quantidades de letras, números e caracteres deve ser igual ao comprimento da senha.")

        senha += ''.join(random.sample(letras, quantidade_letras))
        senha += ''.join(random.sample(numeros, quantidade_numeros))
        senha += ''.join(random.sample(caracteres_especiais, quantidade_caracteres))

        senha = ''.join(random.sample(senha, len(senha)))

        return senha

def obter_pasta_documentos():
    idioma_sistema = locale.getdefaultlocale()[0]

    if idioma_sistema.startswith("pt"):
        return os.path.join(os.path.expanduser("~"), "Documentos")
    else:
        return os.path.join(os.path.expanduser("~"), "Documents")

def gerar_senha_btn_click():
    comprimento_senha = int(comprimento_var.get())
    quantidade_letras = int(quantidade_letras_var.get())
    quantidade_numeros = int(quantidade_numeros_var.get())
    quantidade_caracteres = int(quantidade_caracteres_var.get())

    gerador = GeradorSenha()

    try:
        senha_gerada = gerador.gerar_senha(comprimento_senha, quantidade_letras, quantidade_numeros, quantidade_caracteres)
        senha_gerada_var.set(senha_gerada)

        pasta_documentos = obter_pasta_documentos()
        salvar_senha_arquivo(senha_gerada, pasta_documentos)

        mensagem_var.set("Senha gerada com sucesso!")
    except ValueError as e:
        mensagem_var.set(str(e))

def copiar_senha_btn_click():
    senha_gerada = senha_gerada_var.get()
    if senha_gerada:
        pyperclip.copy(senha_gerada)
        mensagem_var.set("Senha copiada para a área de transferência.")

def salvar_senha_arquivo(senha, pasta_documentos):
    nome_arquivo = os.path.join(pasta_documentos, "senhas.txt")

    try:
        with open(nome_arquivo, "a") as arquivo:
            arquivo.write(senha + "\n")
        print(f"A senha foi salva com sucesso no arquivo {nome_arquivo}.")
    except Exception as e:
        print(f"Erro ao salvar a senha no arquivo: {e}")

app = tk.Tk()
app.title("Gerador de Senhas")
app.geometry("400x300")

frame = ttk.Frame(app, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

comprimento_label = ttk.Label(frame, text="Comprimento da senha:")
comprimento_label.grid(row=0, column=0, sticky=tk.W)
comprimento_var = tk.StringVar(value="12")
comprimento_entry = ttk.Entry(frame, textvariable=comprimento_var)
comprimento_entry.grid(row=0, column=1, padx=5)

quantidade_letras_label = ttk.Label(frame, text="Quantidade de letras:")
quantidade_letras_label.grid(row=1, column=0, sticky=tk.W)
quantidade_letras_var = tk.StringVar(value="6")
quantidade_letras_entry = ttk.Entry(frame, textvariable=quantidade_letras_var)
quantidade_letras_entry.grid(row=1, column=1, padx=5)

quantidade_numeros_label = ttk.Label(frame, text="Quantidade de números:")
quantidade_numeros_label.grid(row=2, column=0, sticky=tk.W)
quantidade_numeros_var = tk.StringVar(value="4")
quantidade_numeros_entry = ttk.Entry(frame, textvariable=quantidade_numeros_var)
quantidade_numeros_entry.grid(row=2, column=1, padx=5)

quantidade_caracteres_label = ttk.Label(frame, text="Quantidade de caracteres especiais:")
quantidade_caracteres_label.grid(row=3, column=0, sticky=tk.W)
quantidade_caracteres_var = tk.StringVar(value="2")
quantidade_caracteres_entry = ttk.Entry(frame, textvariable=quantidade_caracteres_var)
quantidade_caracteres_entry.grid(row=3, column=1, padx=5)

gerar_senha_btn = ttk.Button(frame, text="Gerar Senha", command=gerar_senha_btn_click)
gerar_senha_btn.grid(row=4, column=0, columnspan=2, pady=10)

copiar_senha_btn = ttk.Button(frame, text="Copiar Senha", command=copiar_senha_btn_click)
copiar_senha_btn.grid(row=5, column=0, columnspan=2, pady=10)

mensagem_var = tk.StringVar(value="")
mensagem_label = ttk.Label(frame, textvariable=mensagem_var, wraplength=380, justify=tk.CENTER)
mensagem_label.grid(row=6, column=0, columnspan=2, pady=10)

senha_gerada_var = tk.StringVar(value="")
senha_gerada_label = ttk.Label(frame, textvariable=senha_gerada_var, wraplength=380, justify=tk.CENTER)
senha_gerada_label.grid(row=7, column=0, columnspan=2, pady=10)

app.mainloop()
