import random
import tkinter as tk
from tkinter import messagebox


def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "linguagem", "internet"]
    return random.choice(palavras)


def exibir_forca(palavra, letras_corretas):
    lbl_palavra.config(text=" ".join(letra if letra in letras_corretas else "_" for letra in palavra))


def verificar_letra():
    letra = entry_letra.get().lower()

    if len(letra) != 1 or not letra.isalpha():
        messagebox.showwarning("Aviso", "Digite apenas uma letra válida.")
        return

    if letra in letras_corretas:
        messagebox.showwarning("Aviso", "Você já tentou essa letra antes.")
        return

    if letra in palavra_secreta:
        letras_corretas.append(letra)
        exibir_forca(palavra_secreta, letras_corretas)
        if all(letra in letras_corretas for letra in palavra_secreta):
            messagebox.showinfo("Parabéns", "Você acertou a palavra!")
            root.destroy()
    else:
        tentativas[0] -= 1
        lbl_tentativas.config(text=f"Tentativas restantes: {tentativas[0]}")
        if tentativas[0] == 0:
            messagebox.showinfo("Fim de jogo", f"A palavra era: '{palavra_secreta}'.")
            root.destroy()


def jogar_forca():
    global palavra_secreta, letras_corretas, tentativas

    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = [6]

    lbl_palavra.config(text="")
    lbl_tentativas.config(text="Tentativas restantes: 6")

    exibir_forca(palavra_secreta, letras_corretas)


def fechar_jogo():
    root.destroy()


root = tk.Tk()
root.title("Jogo da Forca")

lbl_palavra = tk.Label(root, font=("Helvetica", 20))
lbl_palavra.pack()

entry_letra = tk.Entry(root, font=("Helvetica", 16))
entry_letra.pack()

btn_verificar = tk.Button(root, text="Verificar", font=("Helvetica", 16), command=verificar_letra)
btn_verificar.pack()

lbl_tentativas = tk.Label(root, text="Tentativas restantes: 6", font=("Helvetica", 14))
lbl_tentativas.pack()

btn_jogar_novamente = tk.Button(root, text="Jogar Novamente", font=("Helvetica", 14), command=jogar_forca)
btn_jogar_novamente.pack()

btn_fechar = tk.Button(root, text="Fechar", font=("Helvetica", 14), command=fechar_jogo)
btn_fechar.pack()

jogar_forca()

root.mainloop()
