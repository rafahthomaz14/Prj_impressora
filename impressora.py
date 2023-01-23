# - pip install pywin32 -    código para instalar no prompt de comando

import win32print
import win32api
import os

# escolher qual impressora a gente vai querer usar
lista_impressoras = win32print.EnumPrinters(2) # mostra todas as impressoras que estao conectada no computador

#for impressora in lista_impressoras:  # organiza a lita de impressoras por linha / código, dirvers, nome da impressora
#print(impressora) 


impressora = lista_impressoras[1]  #o numero da chave significa qual é a impressora que vai usar, numerando de cima pra baixo começando do 0,1,2,3...

win32print.SetDefaultPrinter(impressora[2]) #colocar o numero do nome da ordem da impressora 

# mandar imprimir todos os arquivos de uma pasta
caminho = r"C:\Users\mkt\Desktop\etiqueta teste"# colocar o local que a pasta estiver no computador 
lista_arquivos = os.listdir(caminho)

# https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
for arquivo in lista_arquivos:
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
