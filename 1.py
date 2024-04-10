# Realizar un programa que calcule el área de un triagunlo de esta manera. El programa deberá solicitar al usuario los dos lados y el ángulo que éstos forman (en grados). Ten en cuenta que la función sin() espera que el ángulo se proporcione en radianes. Ángulo en radianes = (ángulo en grados * pi) / 180.
import math
lado1 = float(input("Ingrese el lado del triángulo: "))
lado2 = float(input("Ingrese el lado del triángulo: "))
angulo_grados = float(input("Ingrese el ángulo en grados que forman estos lados: "))

angulo_radianes = (angulo_grados * math.pi) / 180
area = (1/2 * lado1 * lado2 * math.sin(angulo_radianes)) 
print("El área del triángulo es:", area)
