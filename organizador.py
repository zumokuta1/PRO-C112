import os 
import shutil
origen = "C://Users//Joel Botero//Downloads"
hacia = "C://Users//Joel Botero//Desktop//Nueva descarga"

lista_de_archivos = os.listdir(origen)
print(lista_de_archivos)

#Mueve todos los archibos de origen hacia destino.

for archivo in lista_de_archivos:
    name, extension = os.path.splitext(archivo)
    print(name)
    print(extension)

    if extension == " ":
        continue
    if extension in [".gif",".png",".jpg",".jpeg","svg"]:
        shutil.move(os.path.join(origen, archivo), os.path.join(hacia, archivo))
    else:
        continue

print("Archivos movidos")