# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib

#Importo y renombro las librerías numpy y matplotlib.pyplot

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Se desea graficar los valores de "x" e "y" en un gráfico de línea
    # A continuación los datos ya disponibles de "x" e "y" para que utilice:
    
    x = list(range(-10, 11, 1))

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Alumno: Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"

    # Alumno: Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    # Crear acá su gráfico

    #1° Genero la figura (la guardo en la variable fig)

    fig = plt.figure()

    #2° Generó el gráfico 

    ax = fig.add_subplot()

    ax.plot(x, y, color = "g", marker = ".", label = "y = x^2")
    ax.set_facecolor("whitesmoke")      #Configuro el color del fondo del gráfico
    ax.set_title("Función cuadrática")  #Configuro el título
    ax.set_ylabel("Etiqueta eje y")     #Configuro la etiqueta del eje y
    ax.set_xlabel("Etiqueta eje x")     #Configuro la etiqueta del eje x
    ax.legend()                         #Leyenda
    plt.show()                          #Muestro el gráfico
    

    print("terminamos")
