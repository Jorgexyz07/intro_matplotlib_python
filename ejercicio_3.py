# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico

    #1° Genero la figura (la guardo en la variable fig)

    fig = plt.figure()

    #2° Generó el gráfico 

    ax = fig.add_subplot()

    ax.scatter(x, y, color ="b", marker =".", label = "y = tan (x)")    #Creo el gráfico de
    ax.set_facecolor("whitesmoke")               #Configuro el color del fondo del gráfico
    ax.set_title("Función tangente")             #Configuro el título
    ax.set_ylabel("Etiqueta eje y")              #Configuro la etiqueta del eje y
    ax.set_xlabel("Etiqueta eje x")              #Configuro la etiqueta del eje x
    ax.legend()                                  #Leyenda
    plt.show()                                   #Muestro el gráfico

    print("terminamos")
