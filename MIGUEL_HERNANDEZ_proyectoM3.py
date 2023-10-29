import random
""" Primeramente importamos la función random, la cual nos permite
generar números pseudoaleatorios para varias distribuciones"""

import matplotlib.pyplot as plt
""" Posteriormente importamos la función: matplotlib.pyplot (previamente instalada)
para poder crear la generación de gráficos en dos dimensiones, a partir de los
datos de nuestros contenidos"""

def simulacion_maq_galton(canicas_cant, reg_niveles): # Definimos en la función "def" 
    # la función qur utilizaremos.

    resultado = [0] * (reg_niveles + 1) # Creamos las variables paara el resultado y el registro
    # de niveles
    
    for _ in range(canicas_cant): # De acuerdo a la cantidad de canicas con las que contamos, 
        # realizamos una función "for".
        nivel = 0
        for _ in range(reg_niveles):
            if random.random() < 0.5:
                nivel += 1
        resultado[nivel] += 1
    
    return resultado

def histograma_grafica(resultado, reg_niveles):
    plt.bar(range(reg_niveles + 1), resultado)
    plt.xlabel('Registro de Nivel') # Creamos la etiqueta para el eje X.
    plt.ylabel('Número de canicas') # Creamos la etiqueta para el eje Y.
    plt.title('Simulación de la Máquina de Galton') # Creamos la etiqueta pata el título.
    plt.show()

canicas_cant = 3000 # Cantidad de canicas 
reg_niveles = 12 # Número de niveles


resultado = simulacion_maq_galton(canicas_cant, reg_niveles)
histograma_grafica(resultado, reg_niveles)

