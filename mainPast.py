import os
import shutil
import customtkinter as tk
from tkinter import filedialog, messagebox
# função para selecionar a pasta de origem
def selecionar_origem():
    caminho = filedialog.askdirectory()
    entrada_origem.delete(0, tk.END)
    entrada_origem.insert(0, caminho)

# função para selecionar a pasta de destino
def selecionar_destino():
    caminho = filedialog.askdirectory()
    entrada_destino.delete(0, tk.END)
    entrada_destino.insert(0, caminho)

# função para copiar os arquivos PDF
def copiar_pdf():
    # obtendo os caminhos da pasta de origem e de destino
    origem = entrada_origem.get()
    destino = entrada_destino.get()

    # verificando se a pasta de origem existe
    if not os.path.exists(origem):
        messagebox.showerror("Erro", "A pasta de origem não existe!")
        return

    # verificando se a pasta de destino existe
    if not os.path.exists(destino):
        messagebox.showerror("Erro", "A pasta de destino não existe!")
        return

    # iterando sobre os arquivos da pasta de origem
    for arquivo in os.listdir(origem):
        # verificando se o arquivo é um PDF
        if arquivo.endswith(".pdf"):
            # construindo os caminhos completos do arquivo de origem e destino
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino, arquivo)

            # copiando o arquivo para a pasta de destino
            shutil.copy2(caminho_origem, caminho_destino)

    # mensagem de conclusão
    messagebox.showinfo("Concluído", "Arquivos PDF copiados com sucesso!")

# criando a janela principal
janela = tk.CTk()
janela.geometry("410x110")
janela.title("Copiar arquivos PDF")

# criando os widgets da janela
rotulo_origem = tk.CTkLabel(janela, corner_radius=20,text="Pasta de origem:")
entrada_origem = tk.CTkEntry(janela, corner_radius=20)
botao_origem = tk.CTkButton(janela, corner_radius=20, text="Selecionar", command=selecionar_origem)

rotulo_destino = tk.CTkLabel(janela, corner_radius=20, text="Pasta de destino:")
entrada_destino = tk.CTkEntry(janela,  corner_radius=20)
botao_destino = tk.CTkButton(janela, corner_radius=20, text="Selecionar", command=selecionar_destino)

botao_copiar = tk.CTkButton(janela, corner_radius=20, text="Copiar", command=copiar_pdf)

# posicionando os widgets na janela
rotulo_origem.grid(row=0, column=0)
entrada_origem.grid(row=0, column=1)
botao_origem.grid(row=0, column=2)

rotulo_destino.grid(row=1, column=0)
entrada_destino.grid(row=1, column=1)
botao_destino.grid(row=1, column=2)

botao_copiar.grid(row=2, column=1)

# iniciando o loop da janela
janela.mainloop()
