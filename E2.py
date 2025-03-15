'''
E2.Solano Becerra Juan Antonio
Creación de un Editor de Texto Simple (Parte 2)
Objetivo
Desarrollar una aplicación de edición de texto con funciones de abrir, guardar y borrar contenido.

Instrucciones
Se deberá de terminar previo a la entrega del examen las Prácticas 4 y 5 para realizar el Examen 2

Integrar las Prácticas 4 y 5 para finalizar el editor de texto

El editor de texto deberá de contener menús con opciones para abrir, guardar y borrar el texto, además de atajos de teclado para cada acción, además de tener un botón para cambiar de color el texto
'''


# Importación de la biblioteca tkinter, se utiliza para crear interfaces gráficas de usuario (GUI)
#El módulo io provee las facilidades principales de Python para manejar diferentes tipos de E/S. Hay tres diferentes tipos de E/S: texto E/S, binario E/S e E/S sin formato.
from tkinter import *
from tkinter import filedialog as FileDialog
from io import open
from tkinter.colorchooser import askcolor


ruta = ""

def abrir(event=None):
    global ruta
    # Abre el cuadro de diálogo para seleccionar el archivo
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto"
    )
    
    if ruta != "":  # Si se seleccionó un archivo
        with open(ruta, 'r') as fichero:  # Abrimos el archivo con 'open'
            contenido = fichero.read()  # Leemos el contenido del archivo
            texto.delete(1.0, 'end')  # Limpiamos el área de texto
            texto.insert('insert', contenido)  # Insertamos el contenido leído el cuadro de texto
        root.title(ruta + " - mi editor")  # Actualizamos el título de la ventana con la ruta del archivo

def nuevo(event=None):
    global ruta
    root.bind("<n>", nuevo)
    ruta = ""  # Limpiamos la ruta
    texto.delete(1.0, 'end')  # Limpiamos el área de texto
    root.title("Mi editor") 

def guardar(event=None):
    if ruta != "":  # Si ya existe una ruta, guardamos en ese archivo
        contenido = texto.get(1.0, 'end')  # Obtenemos el contenido del área de texto
        with open(ruta, "w+") as fichero:  # Abrimos el archivo para escribir w+
            fichero.write(contenido)  # Escribimos el contenido en el archivo
    else:
        guardar_como()  # Si no hay ruta, pedimos al usuario que le asigne un nombre (guardar como)

def guardar_como(event=None):
    global ruta
    fichero = FileDialog.asksaveasfile(title="Guardar archivo", mode="w", defaultextension=".txt")
    
    if fichero is not None:  # Si se seleccionó un archivo
        ruta = fichero.name  # Obtenemos el nombre del archivo
        contenido = texto.get(1.0, 'end')  # Obtenemos el contenido del área de texto
        with open(ruta, "w+") as fichero:  # Abrimos el archivo para escribir
            fichero.write(contenido)  # Escribimos el contenido en el archivo
    else:
        ruta = ''  # Si no se seleccionó un archivo se limpia la ruta

def cambiar_color_texto(event=None):
    # funcion se abre el cuadro de diálogo para seleccionar un color
    color = askcolor()[1]  # askcolor devuelve una tupla ( estructura datos ligera que tiene un numero especifico), el segundo valor es el código del color seleccionado
    
    if color:  # Si el usuario seleccionó un color
        texto.tag_configure("color_texto", foreground=color)  # Configuramos el color para el texto
        texto.tag_add("color_texto", "1.0", "end")  # Aplicamos el color a todo el texto (desde el principio hasta el final)

def borrar_texto(event=None):
    texto.delete(1.0, 'end') 

def salir(event=None):
    root.quit()


# Configuración de la raíz (ventana principal)
root = Tk()
root.title("Editor de texto simple")


root.bind("<Control-n>", nuevo)
root.bind("<Control-a>", abrir)
root.bind("<Control-g>", guardar)
root.bind("<Alt-c>", cambiar_color_texto)
root.bind("<Alt-e>", borrar_texto)
root.bind("<Control-q>", salir)

# Creación del menú superior
menubar = Menu(root)

# Menú Archivo (se crea un submenú dentro del menú principal)
filemenu = Menu(menubar, tearoff=0)  # tearoff=0 opción que significa que no podrá separarse en una ventana flotante
filemenu.add_command(label="Nuevo (ctrl+N)", command=nuevo)
filemenu.add_command(label="Abrir (ctrl+A)", command=abrir)
filemenu.add_command(label="Guardar (ctrl+G)", command=guardar)
filemenu.add_separator()  # Añade una línea divisora dentro del menú
filemenu.add_command(label="Salir (ctrl+q)", command=root.quit)  # El argumento quit termina el bucle principal y cierra la ventana
menubar.add_cascade(menu=filemenu, label="Archivo")

root.config(menu=menubar)

# Menú texto, se crea otro submenú esta vez debajo del menú texto
menubartexto = Menu(root)
filemenu = Menu(menubartexto, tearoff=0)
filemenu.add_command(label="Color de texto (Alt+C)",command=cambiar_color_texto)
filemenu.add_command(label="Borrar texto (Alt+E)", command=borrar_texto)
filemenu.add_command(label="Buscar y Reemplazar (Alt+B)")
menubar.add_cascade(menu=filemenu, label="Texto")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Aptos Narrow", 12))

root.config(menu=menubar)  # Asocia el menú menubar con la ventana principal root, haciendo que aparezca en la parte superior

# Finalmente, el bucle de la aplicación, línea fundamental en aplicaciones tkinter
root.mainloop()








'''
https://www.youtube.com/watch?v=VIi2QPZlW4g
https://docs.python.org/es/3.9/library/io.html
https://www.youtube.com/watch?v=YkIXrQL4siE

'''