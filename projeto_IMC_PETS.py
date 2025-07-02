import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura_cm = float(entrada_altura.get())
        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)
        especie_selecionada = especie.get()

        if especie_selecionada == "Cachorro":
            if imc < 15:
                categoria = "Abaixo do peso"
                dica = "Aumente a alimentação com rações ricas em proteína."
                imagem_label.config(image=cachorro_abaixo)
                imagem_label.image = cachorro_abaixo
            elif imc <= 25:
                categoria = "Peso ideal"
                dica = "Continue com a alimentação atual e passeios regulares!"
                imagem_label.config(image=cachorro_ideal)
                imagem_label.image = cachorro_ideal
            else:
                categoria = "Acima do peso"
                dica = "Diminua petiscos e aumente a atividade física."
                imagem_label.config(image=cachorro_acima)
                imagem_label.image = cachorro_acima

        elif especie_selecionada == "Gato":
            if imc < 13:
                categoria = "Abaixo do peso"
                dica = "Ofereça mais ração úmida e balanceada."
                imagem_label.config(image=gato_abaixo)
                imagem_label.image = gato_abaixo
            elif imc <= 23:
                categoria = "Peso ideal"
                dica = "Mantenha brinquedos e estímulos em casa!"
                imagem_label.config(image=gato_ideal)
                imagem_label.image = gato_ideal
            else:
                categoria = "Acima do peso"
                dica = "Evite ração à vontade e incentive a brincadeira."
                imagem_label.config(image=gato_acima)
                imagem_label.image = gato_acima

        mensagem = f"IMC: {imc:.2f} - {categoria}\n\nDica: {dica}"
        messagebox.showinfo("Resultado", mensagem)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Interface
janela = tk.Tk()
janela.title("Calculadora IMC Pet")
janela.geometry("400x520")

ttk.Label(janela, text="Nome do Pet:").pack()
entrada_nome = ttk.Entry(janela)
entrada_nome.pack()

ttk.Label(janela, text="Espécie:").pack()
especie = ttk.Combobox(janela, values=["Cachorro", "Gato"], state="readonly")
especie.pack()

ttk.Label(janela, text="Peso (kg):").pack()
entrada_peso = ttk.Entry(janela)
entrada_peso.pack()

ttk.Label(janela, text="Altura (cm):").pack()
entrada_altura = ttk.Entry(janela)
entrada_altura.pack()

ttk.Button(janela, text="Calcular IMC", command=calcular_imc).pack(pady=10)

# Área para imagem
imagem_label = ttk.Label(janela)
imagem_label.pack(pady=10)

# Carrega as imagens
cachorro_abaixo = PhotoImage(file="cachorro_abaixo.gif")
cachorro_ideal = PhotoImage(file="cachorro_ideal.gif")
cachorro_acima = PhotoImage(file="cachorro_acima.gif")
gato_abaixo = PhotoImage(file="gato_abaixo.gif")
gato_ideal = PhotoImage(file="gato_ideal.gif")
gato_acima = PhotoImage(file="gato_acima.gif")

janela.mainloop()