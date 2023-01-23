# - pip install pywin32 -    código para instalar no prompt de comando

import win32print
import win32api
import os
import requests
from tkinter import*

def center(win): # win - janela principal ou janela de nível superior para o centro

    win.update_idletasks()  # Atualize o "tamanho solicitado" do gerenciador de geometria

    # define largura e altura das dimensões da janela
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Obtenha a posição da janela a partir do topo dinamicamente, bem como a posição da esquerda ou direita da seguinte forma
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # esta é a linha que centralizará sua janela
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify() #mostra a janela centralizada na tela 

def imprimir():
    
    lista_impressoras = win32print.EnumPrinters(2)
    impressora = lista_impressoras[1]
    win32print.SetDefaultPrinter(impressora[2])
    win32api.ShellExecute(0, "print", lista, None, caminho, 0)

#for impressora in lista_impressoras:  # organiza a lita de impressoras por linha / código, dirvers, nome da impressora
#print(impressora) 

caminho = r"C:\Users\mkt\Desktop\etiqueta teste"
lista_arquivos = os.listdir(caminho)

for lista in lista_arquivos:
        # comandos que mostra o botao com as legenda 
        arquivo = Tk()
        arquivo.title("Print_PDF")
        arquivo.geometry("230x100")
        center(arquivo)
        texto = Label(arquivo, text="Clique no botão para imprimir arquivos")
        texto.grid(column=0, row=0, padx=10, pady=10)
        botao = Button(arquivo, text="Imprimir",command=imprimir)
        botao.grid(column=0, row=1, padx=10, pady=10)
        texto_resposta = Label(arquivo, text="")
        texto_resposta.grid(column=0, row=2, padx=10, pady=10)

        arquivo.mainloop()

