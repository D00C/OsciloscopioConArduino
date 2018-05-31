# Programa para leer el valor que imprime Arduino en el puerto serial en un arreglo y
# graficarlo en tiempo real, esto es una recompilación de algunos programas encontrados en
# múltiples fuentes de Internet sobre como utilizar las librerías drawnow, serial y
# matplotlib.pyplot así como en los ejemplos encontrados en la documentación de las
# mismas.

# Librería para leer de un puerto serial
import serial
# Librería para hacer el plot
import matplotlib.pyplot as plt
# Librería para graficar en tiempo real
from drawnow import *

# Función para actualizar la gráfica en tiempo real
def MakeFig():                  
    # Definir limites para Y
    plt.ylim(-10,10)
    # Definir límites para X
    plt.xlim(0,50)
    # Titulo de la gráfica
    plt.title('Osciloscopio')
    # Colocar la rejilla
    plt.grid()
    # Titulo para Y
    plt.ylabel('Volts')
    # Gráfica  del arreglo
    plt.plot(VOLT, 'ro-')

# Crear un objeto serial para los datos
ArduinoData = serial.Serial("/dev/ttyACM0", 115200)
VOLT = []
X = []
# Le dice a matplotlib que inicie en modo interactivo
plt.ion()

# Ciclo que continua para siempre
while True:
    # Leer una linea de texto del puerto serial
    ArduinoString = ArduinoData.readline()
    # Arduino arroja algunos datos que no pueden ser convertidos a float de forma
    # aparentemente aleatoria, por esto decidimos utilizar un try: except: que intente
    # correr el siguiente código y de ocurrir un error por los datos no hacer nada en ese
    # ciclo.
    try:
        # Convertir el texto a float y cambiarlo según el análisis de los datos
        Volt = 8*(float(ArduinoString) - 2.5)
        # Agregar datos al arreglo para el plot
        VOLT.append(Volt)
        # LLama a drawnow para actualizar el plot con la función MakeFig descrita
        # anteriormente
        drawnow(MakeFig)
        # Condicional para leer el largo del arreglo y preguntar si es mayor a 50
        # elementos
        if len(VOLT) > 50:
            # Eliminar el primer elemento
            VOLT.pop(0)
    except:
        # Esto solo salta el ciclo en caso de un error
        pass
