"""
6. Embaldosado de Sierpinski
    No terminales: F G
    Terminales: + −
    Cadena Inicial: F
    Reglas de producción :  (F→F+F-F-F-G+F+F+F-F)
                            (G → GGG)
    Angulo : 90°
    Interpretación:
        F: Dibujar Segmento
        +: Girar a la Izquierda
        -: Girar a la Derecha
"""
from turtle import *  #se va a codigo no orientado a objetos
#import turtle #orientado a objetos

def dibujar(cadena):
    lst = separarCamino(cadena)
    for pivote in lst:
        if pivote == 'F' or pivote == 'G':
            if pivote == 'F':
                pencolor(0, 0, 205)
            else:
                pencolor(199, 21, 133)
            forward(longitud)   #dibujo la linea
        elif pivote =='+':  left(angulo)    #la tortuga gira a la izquierda
        elif pivote == '-': right(angulo)   #la tortuga gira a la derecha

def separarCamino(cadena):
    i = 0
    lst = []    #creamos una lista
    while i < len(cadena):
        if cadena[i] == "F":
            lst.append(cadena[i:i+1]) #lo agregamos a la lista
        else:
            lst.append(cadena[i]) #agregamos a la lista 
        i= i + 1
    return lst

def iniciarProduccion(cadena, regla):
    lst = separarCamino(cadena)
    #por cada posicion de la list
    for i in range(len((lst))):
        pivote = lst[i]
        if pivote in regla:         #evalua si el pivote es miembro de la regla
            lst[i] = regla[pivote]  # le mando la regla    
    #Devuelve uniendo todos los elementos separados
    cadena = "".join(pivote for pivote in lst)
    return cadena

bgcolor("black")    #color de fondo
colormode(255)      #rama del color creo ajaj
#speed(0)            #velocidad de la tortuga 0-instantaneo 1- muy, muy lento
pensize(4)          #tamanio de la tortuga

title("EMBALDOSADO DE SIERPINKSI")
screensize(50000, 20800)  #barra de desplazamiento
shape("turtle")
setpos(-300,0)

#GRAMATICA DE LINDENMAYER a
axiom = "F"    #cadena inicial
angulo = 90         #Angulo
#creamos diccionario
reglaProduccion = {
    #EMBALDOSADO DE SIERPINKSI
    "F": "F+F-F-F-G+F+F+F-F",
    "G": "GGG"

    #TRIANGULO DE SIERPINSKI
    #"F": "F-G+F+G-F",
    #"G": "GG"
}

longitud = 50        #largo del segmento
iteracion = int(input("Ingrese el numero de iteraciones: "))       #numero de iteracion

#un for por cada iteracion
for i in range(iteracion):
    print("\nANTES DE LA PRODUCCION " + axiom)
    axiom = iniciarProduccion(axiom,reglaProduccion)
    print("DESPUES DE LA PRODUCCION" + axiom + "\n")

print("A DIBUJAR!!!")
dibujar(axiom)
print("DIBUJO TERMINADO")
input("Press enter to close program")