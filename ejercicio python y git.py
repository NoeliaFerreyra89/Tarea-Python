#EJERCICIO 1
def calcular_promedio(notas) :
    suma =sum(notas)
    promedio= suma/len(notas)
    return promedio
notas= [7, 4, 10, 8, 6]
promedio = calcular_promedio(notas)
print('Elpromedio es :' , promedio)

#EJERCICIO 2
def es_color_primario(color):
    colores_primarios = ['rojo', 'verde', 'azul']
    if color in colores_primarios:
        print(f"El color {color} es un color primario.")
    else:
        print(f"El color {color} no es un color primario.")
es_color_primario('rojo')   
es_color_primario('marron')  

#EjERCICIO 3
def numero_mayor(lista):
    mayor = max(lista)
    print(f"El número mayor de la lista es: {mayor}")
    return mayor
lista = [15, 5, 97, 4, 88, 35]
numero_mayor(lista) 

#EJERCICIO 4
def dibujar_rectangulo(filas, columnas):
    for i in range(filas):
        print('*' * columnas)
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
dibujar_rectangulo(filas, columnas)

#EJERCICIO 5
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  
    return factorial
numero = int(input("Ingrese un número entero positivo: "))
resultado = calcular_factorial(numero)
if resultado is not None:
    print(f"El factorial de {numero} es: {resultado}")
