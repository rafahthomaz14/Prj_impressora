# - pip install pywin32 -    código para instalar no prompt de comando

import win32print
import win32api
#import os

# escolher qual impressora a gente vai querer usar
lista_impressoras = win32print.EnumPrinters(2) # mostra todas as impressoras que estao conectada no computador

for impressora in lista_impressoras:  # organiza a lita de impressoras por linha / código, dirvers, nome da impressora

    print(impressora)
