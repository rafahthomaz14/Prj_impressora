# - pip install pywin32 -    código para instalar no prompt de comando

import win32print
import win32api
import os
import requests
from tkinter import*


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


    arquivo = Tk()
    arquivo.title("Print_PDF")
    texto = Label(arquivo, text="Clique no botão para imprimir arquivos")
    texto.grid(column=0, row=0, padx=10, pady=10)
    botao = Button(arquivo, text="Imprimir",command=imprimir)
    botao.grid(column=0, row=1, padx=10, pady=10)
    texto_resposta = Label(arquivo, text="")
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)



    arquivo.mainloop()

#cod_rafae>hthomaz_1
