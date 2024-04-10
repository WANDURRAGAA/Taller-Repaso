# crear un programa que a, b y c sean tres variables enteras que representan las ventas de tres productos a, b, c, respectivamente. Utilizando dichas variables, escribir un código que permita mostrar las siguientes expresiones

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

# a) Las ventas del producto _ son las más elevadas
if a > b and a > c:
    print("Las ventas del producto a son las más elevadas")
elif b > a and b > c:
    print("Las ventas del producto b son las más elevadas")
else:
    print("Las ventas del producto c son las más elevadas")
    
# b) Cuantos productos tienen ventas inferiores a 200?
if a < 200:
    print("El producto a tiene ventas inferiores a 200")
if b < 200:
    print("El producto b tiene ventas inferiores a 200")
if c < 200:
    print("El producto c tiene ventas inferiores a 200")

#c) Algún producto tiene ventas superiores a 400?
if a > 400:
    print("El producto a tiene ventas superiores a 400")
if b > 400:
    print("El producto b tiene ventas superiores a 400")
if c > 400:
    print("El producto c tiene ventas superiores a 400")

# d) La media de ventas es superior a 500?
media = (a + b + c) / 3
if media > 500:
    print("La media de ventas es superior a 500")
else:
    print("La media de ventas es inferior a 500")

# e) El producto __ no es el más vendido
if a < b and a < c:
    print("El producto a no es el más vendido")
elif b < a and b < c:
    print("El producto b no es el más vendido")
else:
    print("El producto c no es el más vendido")
    
# f) El total de ventas esta entre 500 y 1000?
if a + b + c > 500 and a + b + c < 1000:
    print("El total de ventas esta entre 500 y 1000")
else:
    print("El total de ventas no esta entre 500 y 1000")
    