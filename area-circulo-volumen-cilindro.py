import math

def areaCirculo(radio):
    area = math.pi * radio**2
    return area

def volumenCilindro(areaCirculo, altura):
    volumen = areaCirculo * altura
    return volumen

radio = float(input("Ingrese el valor del radio: "))
altura = float(input("Ingrese el valor de la altura: "))
areaDelCirculo = areaCirculo(radio)
volumenDelCilindro = volumenCilindro(areaDelCirculo, altura)

print("El area del circulo es:", areaDelCirculo, "\nEl volumen del cilindro es: ", volumenDelCilindro)

