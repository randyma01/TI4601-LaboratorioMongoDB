"""
----------------------------------------------------------------------

Área Académica de Administración de Tecnología de Información

Curso:
    Bases de Datos Avanzados - TI4601

Tarea:
    Laboratorio MongoDB

Fecha:
    7 de octubre, 2018
    Semestre II

Estudiante:
	Randy Martínez Sandí

Carnet: 2014047395

Índice:
    1. Importación de la librerías utilizadas.
    2. Declaración de funciones auxiliares de uso global.
    3. Desarrollo de la interfaz gráfica.

Nota:
    El siguiente código corresponde únicamente a la parte de la
    aplicación (UI).
----------------------------------------------------------------------
"""
#-------------------------------------------------------------------#
#-----------------------Bilbiotecas Utilizadas----------------------#
#-------------------------------------------------------------------#

# Libreria para la Interfaz Gr[afica #
import tkinter
from tkinter import *
from tkinter import messagebox

# Librería para utilizar los recursos del OS #
import os

# Librería de la Conexión y control de la Parte de MongoDB #
# (este archivo corresponde a la otra parte del laboratrio #
# y se encuentre en este mismo folder )                    #
from connection import *

#-------------------------------------------------------------------#
#----------------------Funciones Auxiliares-------------------------#
#-------------------------------------------------------------------#

# Cargar Imagenes #
def cargarImagen(nombre):
    ruta = os.path.join('imagenes',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

# Terminar el Programa #
def salida():
    return exit

#-------------------------------------------------------------------#
#--------------------------Parte Grafica----------------------------#
#-------------------------------------------------------------------#


#-----Ventana de Consultas-----#
def ventanaConsultas():
    ventanaPrincipal.withdraw()
    ventanaConsultas = Toplevel()
    ventanaConsultas.title("Consultas a MovieDB")
    ventanaConsultas.minsize(800,550)
    ventanaConsultas.resizable(width=NO,height=NO)

    # Imagen de Fondo Ventana Consultas #
    imagenConsultas = cargarImagen("sala_cine.gif")
    imagenVentanaConsultas=Label(ventanaConsultas, image=imagenConsultas, bg = "#000000")
    imagenVentanaConsultas.place (x=0, y=0)

    # Canva Consultas #
    contenedorConsultas = Canvas(ventanaConsultas , width= 1000, height = 800, bg = "#000000")
    contenedorConsultas.place(x=0,y=0)

    # Titulo Consultas #
    tituloConsultas = Label(ventanaConsultas,text="Ejecute sus Consultas", fg="#FFFFFF", bg ="#000000", font=("Courier",40))
    tituloConsultas.place(x=150,y=25)

    #----Opciones de Consulta----#

    #--Consultar Pelicula por Nombre--#
    infoPeliculaNombre = Label(ventanaConsultas,text="-> Consultar película por nombre: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaNombre.place(x=25,y=100)
    entradaNombre = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaNombre.place(x=400,y=100)

    def ejecutarConsultaNombre():
        temp = str(entradaNombre.get())
        res = consultarPeliculaNombre(temp)
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaNombre = Button(ventanaConsultas, command=ejecutarConsultaNombre, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaNombre.place(x=570,y=100)
    

    #--Consultar Pelicula por Franquicia--#
    infoPeliculaFranquicia = Label(ventanaConsultas,text="-> Consultar película por franquicia: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaFranquicia.place(x=25,y=150)
    entradaFranquicia = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaFranquicia.place(x=440,y=150)

    def ejecutarConsultaFranquicia():
        temp = str(entradaFranquicia.get())
        res = consultarPeliculaFranquicia(temp)
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaFranquicia = Button(ventanaConsultas, command=ejecutarConsultaFranquicia, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaFranquicia.place(x=570,y=150)

    #--Consultar Pelicula por Años--#
    infoPeliculaAhnos = Label(ventanaConsultas,text="-> Consultar película por año: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaAhnos.place(x=25,y=200)
    entradaAhnos1 = Entry(ventanaConsultas, width=5, bg = "#FFFFFF")
    entradaAhnos1.place(x=370,y=200)
    entradaAhnos2 = Entry(ventanaConsultas, width=5, bg = "#FFFFFF")
    entradaAhnos2.place(x=440,y=200)

    def ejecutarConsultaAhnos():
        temp1 = entradaAhnos1.get()
        temp2 = entradaAhnos2.get()
        res = consultarPeliculaAhnos(temp1, temp2)
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaAhno= Button(ventanaConsultas, command=ejecutarConsultaAhnos, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaAhno.place(x=570,y=200)

    #--Consultar Pelicula por productora--#
    infoPeliculaProductora = Label(ventanaConsultas,text="-> Consultar película por productora: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaProductora.place(x=25,y=250)
    entradaProductora = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaProductora.place(x=440,y=250)
    botonConsultaProductora= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaProductora.place(x=570,y=250)

    #--Consultar Duracion Minima--#
    infoPeliculaDuracionMinima = Label(ventanaConsultas,text="-> Consultar información de la duración minima ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracionMinima.place(x=25,y=300)
    botonConsultaDuracionMinima= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracionMinima.place(x=570,y=300)

    #--Consultar Duracion Maxima--#
    infoPeliculaDuracionMaxima = Label(ventanaConsultas,text="-> Consultar información de la duración maxima ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracionMaxima.place(x=25,y=350)
    botonConsultaDuracionMaxima= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracionMaxima.place(x=570,y=350)

    #--Consultar Duracion Promedio--#
    infoPeliculaDuracionPromedio = Label(ventanaConsultas,text="-> Consultar información de la duración promedio ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracionPromedio.place(x=25,y=400)
    botonConsultaDuracionPromedio= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracionPromedio.place(x=570,y=400)


    #----------------------------#


    # Funcion para regresar a Ventana Principal 
    def regresarVentanaPrincipal():
        ventanaConsultas.destroy()
        ventanaPrincipal.deiconify()

    # Boton para regresar a la Ventana Principal #
    botonReresoVentanaPrincipal = Button(ventanaConsultas, command=regresarVentanaPrincipal, text="SALIDA", bg="#FFFFFF", fg="#FE0000", font=("Courier",28))
    botonReresoVentanaPrincipal.place(x=355,y=450)


#-----Ventana Principal-----#
ventanaPrincipal = Tk()
ventanaPrincipal.title("MovieDB")
ventanaPrincipal.minsize(800,600)
ventanaPrincipal.resizable(width=NO,height=NO)
ventanaPrincipal.geometry("800x600+250+50")

# Canva Principal #
contenedorPrincipal = Canvas(ventanaPrincipal , width= 800, height = 700, bg = "#000000")
contenedorPrincipal.place(x=0,y=0)

# Imagen de Fondo Ventana Principal #
imagenPrincipal = cargarImagen("entrada_cine.gif")
imagenVentanaPrincipal=Label(ventanaPrincipal, image=imagenPrincipal, bg = "#FFFFFF")
imagenVentanaPrincipal.place (x=0, y=0)

# Titulo Ventana Principal #
tituloPrincipal = Label(ventanaPrincipal,text="MovieDB", fg="#000000", bg ="#FFFFFF", font=("Courier",55))
tituloPrincipal.place(x=285,y=95)

# Boton para ir a Ventana de Consultas #
botonConsultas = Button(ventanaPrincipal, command=ventanaConsultas, text="Consultas", bg = "#000000", fg = "#000000", font=("Courier",30))
botonConsultas.place(x=315,y=225)

# Boton para ir a Ventana de Insertar #
botonInsertar = Button(ventanaPrincipal, command=ventanaConsultas, text="Insertar", bg = "#000000", fg = "#000000", font=("Courier",30))
botonInsertar.place(x=325,y=275)

# Boton para ir a Ventana de Actualizar #
botonInsertar = Button(ventanaPrincipal, command=ventanaConsultas, text="Actualizar", bg = "#000000", fg = "#000000", font=("Courier",30))
botonInsertar.place(x=310,y=325)

# Boton para terminar del Programar #
botonSalida = Button(ventanaPrincipal, command=salida(), text="SALIDA", bg="#FFFFFF", fg="#FE0000", font=("Courier",28))
botonSalida.place(x=345,y=475)

