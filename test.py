       etiqueta= r"C:\Users\ADM\Desktop\etiquetas"

        for root,dirs,file in os.walk(etiqueta):

            for file in files:
                new_file_path = os.path.join(etiqueta,file)

        if '.pdf' in file:
            os.remove(new_file_path)

