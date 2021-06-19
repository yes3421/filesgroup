import os
from time import sleep
import threading
import shutil
import random


#Esta es la funcion que carga la data
def data_load(cont):
    cont = cont.split("\n")
    cont.remove("")
    dic = {}
    for l in cont:
        if cont.index(l) == 0:
            path = l
        else:
            line = l.split("|")
            temp = line[0]
            line.remove(line[0])
            dic[temp] = line


    return path, dic

#este se encarga de buscar las caprtetas
def search():
    try:
        listd = os.listdir(os.environ['HOMEPATH'])
        listd = os.listdir(os.environ['HOMEPATH'])
        listd = [x for x in listd if x in ["Documents", "Desktop", "Pictures", "Music", "Videos", "3D Objects"]];
        format_dic = {"C:" + os.environ['HOMEPATH'] + "\\" + "Documents" : [],
                "C:" + os.environ['HOMEPATH'] + "\\" + "Desktop" : [],
                "C:" + os.environ['HOMEPATH'] + "\\" + "Pictures" : [],
                "C:" + os.environ['HOMEPATH'] + "\\" + "Music" : [],
                "C:" + os.environ['HOMEPATH'] + "\\" + "Videos" : [],
                "C:" + os.environ['HOMEPATH'] + "\\" + "3D Objects" : []}
        if not listd:
            listd = os.listdir(os.environ['HOMEPATH'])
            listd = [x for x in listd if x in ["Documentos", "Escritorio", "Imágenes", "Música", "Vídeos", "Objetos 3D"]];
            format_dic = {"C:" + os.environ['HOMEPATH'] + "\\" + "Documentos" : [],
                    "C:" + os.environ['HOMEPATH'] + "\\" + "Escritorio" : [],
                    "C:" + os.environ['HOMEPATH'] + "\\" + "Imágenes" : [],
                    "C:" + os.environ['HOMEPATH'] + "\\" + "Música" : [],
                    "C:" + os.environ['HOMEPATH'] + "\\" + "Vídeos" : [],
                    "C:" + os.environ['HOMEPATH'] + "\\" + "Objectos 3D" : []}
            os.chdir(path = "C:" + os.environ['HOMEPATH'] + "\\" + "Downloads")


        else:
            path = "C:" + os.environ['HOMEPATH'] + "\\" + "Downloads"

    except:
        print("Error sistema no compatible")
        os.system("PAUSE")
        exit()

    return path, format_dic


#Esta es la funcion que se encarga de ver
#Si tienes ya una configuracion cargada o no
def documents():
    try:
        filed = open('config.txt', 'r')
        cont = filed.read()
        filed.close()
        return cont, 1


    except:
        filed = open('config.txt', 'w')
        filed.close()
        return "", 0


#este hace un cambio en la ruta raiz
def cambio_de_carpeta(original_path):
    while True:
        os.system("cls")
        print("Ruta actual: ", original_path)
        temp = input("Coloca literalmente la ruta de la carpeta donde vas a recibir las descargas: ")
        if os.path.exists(temp):
            original_path = temp
            break

        else:
            print("Debes de colocar un path que exista ")
            sleep(2)
    return original_path


#esta es la funcion que hace cambios en las rutas y los paths
def cambio_formatos_paths(path, dic):
    while True:
        os.system("cls")
        for key in dic:
            print("Para el " + key + ": ",end="")
            for i in dic[key]:
                print(i + " ", end="")
            print("")

        print("\nQue quieres hacer: ")
        print("Puedes agregar,  modificar y eliminar cualquier formato o carpeta")
        print("[1] Eliminar")
        print("[2] Modificar")
        print("[3] Agregar")
        print("[4] Regresar")

        input_user = input("\n>>> ")
        if input_user == "1":
            while True:
                os.system("cls")
                for key in dic:
                    print("Para el " + key + ": ",end="")
                    for i in dic[key]:
                        print(i + " ", end="")
                    print("")
                print("\nQue quieres eliminar una ruta o un formato ")
                print("[1] ruta")
                print("[2] formato")
                print("[3] regresar")
                action = input(">>> ")
                if action == "1":
                    print("Coloque exactamente la ruta: ")
                    ruta = input("Ruta: ")
                    encontro = False
                    for key in dic:
                        if ruta == key:
                            encontro = True
                            del dic[ruta]
                            break;
                    if encontro:
                        print("Ruta eliminada ")
                    else:
                        print("No se encontro la ruta")

                    input("Presione Enter")

                elif action == "2":
                    print("Coloque exactamente el formato: ")
                    formato = input("Formato: ")
                    encontro = False
                    for key in dic:
                        for f in dic[key]:
                            if f == formato:
                                encontro = True
                                del dic[key][dic[key].index(f)]
                    if encontro:
                        print("Formato eliminado")
                    else:
                        print("No se encontro archivo")

                    input("Presione enter")

                elif action == "3":
                    break;



        elif input_user == "2":
            while True:
                os.system("cls")
                for key in dic:
                    print("Para el " + key + ": ",end="")
                    for i in dic[key]:
                        print(i + " ", end="")
                    print("")
                print("\nQue quieres modificar una ruta o un formato ")
                print("[1] ruta")
                print("[2] formato")
                print("[3] regresar")
                action = input(">>> ")
                if action == "1":
                    encontro = False
                    print("Coloque exactamente la ruta ")
                    root = input("Ruta: ")
                    for key in dic:
                        if root == key:
                            encontro = True
                            print("Coloque la nuva ruta: ")
                            new_root = input("Nueva Ruta: ")
                            break
                    if not encontro:
                        print("No tienes agregada esa ruta")
                        sleep(2)

                elif action == "2":
                    print("Coloque exactamente el formato: ")
                    encontro = False
                    formato = input("Formato: ")
                    for key in dic:
                        for f in dic[key]:
                            if f == formato:
                                encontro = True
                                print("Formato encontrado")
                                new_f = input("Coloca el nuevo formato: ")
                                dic[key][dic[key].index(f)] = new_f
                    if not encontro:
                        print("No se encontro ese formato")
                        sleep(2)

                elif action == "3":
                    break



        elif input_user == "3":
            while True:
                os.system("cls")
                for key in dic:
                    print("Para el " + key + ": ",end="")
                    for i in dic[key]:
                        print(i + " ", end="")
                    print("")
                print("\nQue quieres agregar una ruta nueva o un formato nuevo")
                print("[1] ruta")
                print("[2] formato")
                print("[3] regresar")
                action = input("\n>>> ")
                if action == "1":
                    print("Coloque una ruta presisa y que exista: ")
                    new_root = input("Ruta: ")
                    if os.path.exists(new_root):
                        dic[new_root] = []
                        print("Ruta agregada.")

                    else:
                        print("Esa ruta no existe")
                        sleep(2)

                    input("Presione enter: ")

                elif action == "2":
                    encontro = False
                    print("Coloca exactamente la ruta a la cual quieres agregar un formato: ")
                    new_root = input("Ruta: ")
                    if os.path.exists(new_root):
                        for key in dic:
                            if key == new_root:
                                print(key)
                                encontro = True
                                print("Print coloca el nuevo formato")
                                form = input("formato: ")
                                existe = False
                                for key2 in dic:
                                    if form in dic[key2]:
                                        print("Ese formato ya existe en otra ruta no puedes tener dos formatos iguales en dos rutas  agrega otro formato o elimina el otro primero")
                                        existe = True
                                        break
                                if not existe:
                                    dic[key].append(form)
                                    print("Formato agregado.")
                                break


                        if not encontro:
                            print("Esa ruta no esta agregada")
                            sleep(2)

                    else:
                        print("Esa ruta no existe")
                        sleep(2)
                    input("Presione enter.")

                elif action == "3":
                    break


        elif input_user == "4":
            break;

    return dic



#esta es la funcion que gurada los cambios en el archivo
def save(path, dic):
    os.system("cls")
    file = open('config.txt', 'w')
    file.write(str(path + "\n"))
    root = "C:" + os.environ['HOMEPATH'] + "\\"
    for key in dic:
        file.write(str(key + "|"))
        for f in dic[key]:
            if dic[key].index(f) == len(dic[key]) - 1:
                file.write(str(f))

            else:
                file.write(str(f + "|"))
        file.write(str("\n"))

    file.close()





#Esta es la clase que tiene los metodos del programa
#y la que carga la configuracion
class con:
    def __init__(self):
        self.cont, self.num = documents()
        if self.num == 0:
            self.path, self.format_dic = search()
            self.config_new()


        else:
            self.path, self.format_dic = data_load(self.cont)


    def config_new(self):
        while True:
            os.system("cls")
            print("Configuracion nueva, elige una opcion de configuracion ")
            print("[1] Quiere usar la configuracion predefinida ? ")
            print("[2] Modifica la configuracion predefinida ?\n")

            input_user = input(">>> ")
            root = "C:" + os.environ['HOMEPATH'] + "\\"
            for key in self.format_dic:
                if key == root + "Documents" or key == root + "Documentos":
                    self.format_dic[key] = [".pdf", ".docx", ".doc", ".txt", ".dot", ".ppt", ".xls", ".xlsx", ".xlsm", ".xlt", ".pptx", ".pps", ".pot"]
                elif key == root + "Music" or key == root + "Música":
                    self.format_dic[key] = [".mp3", ".wav", ".aiff", ".wma", ".ogg", ".opus", ".flac", ".alac", ".aac"]

                elif key == root + "Pictures"  or key == root + "Imágenes":
                    self.format_dic[key] = [".jpg", ".png", ".gif", ".jpeg", ".tif", ".tiff", ".svg"]

                elif key == root + "Videos" or key == root + "Vídeos":
                    self.format_dic[key] = [".avi", ".mov", ".wmv", ".mp4", ".flv", ".mpeg", ".mkv"]

                elif key == root + "3D Objects" or key == root + "Objetos 3D":
                    self.format_dic[key] = [".fbx", ".dae", ".3ds", ".dxf", ".obj"]

                elif key == root + "Escritorio" or key == root + "Desktop":
                    self.format_dic[key] = [".rar", ".zip", ".gz", ".tar", ".bz2", ".7z"]

            if input_user == "1":
                os.system("cls")
                print("La configuracion actual es ")
                print("La carpeta de descargas es: ", self.path)
                print("\n\nEn base a los formatos de los archivos se van a mover: ")
                print("___________________________________________________________")
                for key in self.format_dic:
                    print("Para el " + key + ": ",end="")
                    for i in self.format_dic[key]:
                        print(i + " ", end="")
                    print("")
                print("___________________________________________________________")
                input("\n\nPresiona Enter para continuar ")
                save(self.path, self.format_dic)
                break

            elif input_user == "2":
                while True:
                    os.system("cls")
                    print("La configuracion actual es:")
                    print("La carpeta de descargas es: ", self.path)
                    print("En base a los formatos de los archivos se van a mover: ")
                    for key in self.format_dic:
                        print(str("Para la carpeta " + key + ": "),end="")
                        for i in self.format_dic[key]:
                            print(i + " ", end="")

                        print("")
                    print("\n[1] modifcar la ruta de la carpeta: ")
                    print("[2] modificar los formatos de los archivos:")
                    print("[3] aceptar esta configuracion y continuar: ")

                    action = input("\n>>> ")

                    if action == "1":
                        self.path = cambio_de_carpeta(self.path)
                        save(self.path, self.format_dic)

                    elif action == "2":
                        self.format_dic = cambio_formatos_paths(self.path, self.format_dic)
                        save(self.path, self.format_dic)

                    elif action == "3":
                        break
                break


            else:
                print("Tienes que colocar 1 o 2")
                sleep(1)



    def config_modify(self):
        while True:
            os.system("cls")
            print("La configuracion actual es:")
            print("La carpeta de descargas es: ", self.path)
            print("En base a los formatos de los archivos se van a mover: ")
            for key in self.format_dic:
                print("Para la carpeta " + key + ": ",end="")
                for i in self.format_dic(key):
                    print(i + " ", end="")
                print("")
            print("\n[1] modifcar la ruta de la carpeta: ")
            print("[2] modificar los formatos de los archivos")
            print("[3] guardar esta configuracion")

            input_user = input("\n>>> ")

            if input_user == "1":
                self.path = cambio_de_carpeta(self.path)

            elif input_user == "2":
                self.format_dic = cambio_formatos_paths(self.format_dic)

            elif input_user == "3":
                break


class Running:
    def __init__(self, corriendo):
        self.corriendo = corriendo

    def programa(self, dic, path):
        while self.corriendo:
            listaf = os.listdir(path)
            for fi in listaf:
                for key in dic:
                    for fo in dic[key]:
                        if fi.endswith(fo):
                            try:
                                shutil.move(path + "\\" + fi, key)

                            except:
                                if fi[len(fi) - 4] == ".":
                                    fe = fi[0 : len(fi) - 4] + str(random.randint(0, 100000)) + fi[len(fi) - 4 : len(fi)]
                                elif fi[len(fi) - 5] == ".":
                                    fe = fi[0 : len(fi) - 5] + str(random.randint(0, 100000)) + fi[len(fi) - 5 : len(fi)]
                                elif fi[len(fi) - 2] == ".":
                                    fe = fi[0 : len(fi) - 2] + str(random.randint(0, 100000)) + fi[len(fi) - 2 : len(fi)]
                                elif fi[len(fi) - 3] == ".":
                                    fe = fi[0 : len(fi) - 3] + str(random.randint(0, 100000)) + + fi[len(fi) - 3 : len(fi)]
                                try:
                                    os.rename(path + "\\" + fi, path + "\\" + fe)

                                except:
                                    pass








#esta es la funcion run la que inicia el programa y lo mantiene
def run():
    config = con()
    while True:
        os.system("cls")
        print("Quieres iniciar programa o quieres salir: ")
        print("[1] iniciar")
        print("[2] modificar")
        print("[3] salir")

        input_user = input("\n>>> ")

        if input_user == "1":
            running = Running(True)
            thread1 = threading.Thread(target = running.programa, args = (config.format_dic, config.path))
            thread1.start()
            while True:
                os.system("cls")
                print("Escuchando en los archivos en el formato {} ".format(config.path))
                print("Queres dentener el programa coloca 'y' y da enter")
                action = input("\n>>> ")
                if action == "y":
                    running.corriendo = False
                    break

                elif action == "n":
                    pass

                else:
                    print("Tienes que poner y o n")
                    sleep(2)


        elif input_user == "2":
            while True:
                os.system("cls")
                print("La configuracion actual es:")
                print("La carpeta de descargas es: ", config.path)
                print("En base a los formatos de los archivos se van a mover: ")
                for key in config.format_dic:
                    print(str("Para la carpeta " + key + ": "),end="")
                    for i in config.format_dic[key]:
                        print(i + " ", end="")

                    print("")
                print("\n[1] modifcar la ruta de la carpeta: ")
                print("[2] modificar los formatos de los archivos:")
                print("[3] aceptar esta configuracion y continuar: ")

                action = input("\n>>> ")

                if action == "1":
                    config.path = cambio_de_carpeta(config.path)
                    save(config.path, config.format_dic)

                elif action == "2":
                    config.format_dic = cambio_formatos_paths(config.path, config.format_dic)
                    save(config.path, config.format_dic)

                elif action == "3":
                    break



        elif input_user == "3":
            os.system("cls")
            exit()




if __name__ == "__main__":
    run()
