import tkinter as tk

root = tk.Tk()

# Cria um rótulo
label = tk.Label(root, text="quantos cliente você possui?")
label.pack()
label = tk.Label(root, text="quanto cada cliente paga ?")
label.pack()

# Cria uma caixa de entrada
entry = tk.Entry(root)
entry.pack()

# Função para imprimir o que foi digitado
def imprimir_dados():
    print("Os dados inseridos foram:", entry.get())

# Cria um botão
button = tk.Button(root, text="Enviar", command=imprimir_dados)
button.pack()

root.mainloop()