import shutil

caminho_original = 'C:\Users\mkt\Desktop\'
caminho_novo = ''


  for root,dirs,files in os.walk(caminho_novo):

            for file in files:
                old_file_path = os.path.join(root,file)
                new_file_path = os.path.join(caminho_novo,file)

        if '.pdf' in file:
            os.remove(new_file_path)
