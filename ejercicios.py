def calcular_area_del_rectanguulo(base, altura):
    area = base * altura
    return area

def cadena_inversa(cadena):
    return cadena[::-1]

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def argumentos_operaciones(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"
    

print("ingrese su nombre:")
nombre = input()
print("Hola, " + nombre + " pura vida!")

num1= 5
num2= 10
suma= num1 + num2
print("La suma de " + str(num1) + " y " + str(num2) + " es: " + str(suma))
resta= num2 - num1
print("La resta de " + str(num2) + " y " + str(num1) + " es: " + str(resta))
multiplicacion= num1 * num2 
print("La multiplicación de " + str(num1) + " y " + str(num2) + " es: " + str(multiplicacion))
division= num2 / num1
print("La división de " + str(num2) + " y " + str(num1) + " es: " + str(division))

nombre1= input("Tacaco")
apellido= input("IQ")
edad1= 18

print("Su nombre es: " + nombre1 + " " + apellido + " y su edad es: " + str(edad1))

print("Ingrese un número entero:")
if __name__ == "__main__":
    numero = int(input())
    if numero % 2 == 0:
        print("El número " + str(numero) + " es par.")
    else:
        print("El número " + str(numero) + " es impar.")

print("ingrese el primer número:")
numA = int(input())
print("ingrese el segundo número:")
numB = int(input())
if numA > numB:
    print("El número mayor es: " + str(numA))
elif numB > numA:
    print("El número mayor es: " + str(numB))
else:
    print("Los números son iguales.")


print("los numeros del 1 al 10 son:")
for i in range(1, 11):
    print(i)

print("la suma de todos los numeros del 1 al 50 es:")
suma_total = 0
for i in range(1, 51):
    suma_total += i
print(suma_total)

contraseña_correcta = "ocar"
while True:
    print("Ingrese la contraseña:")
    contraseña_ingresada = input()
    if contraseña_ingresada == contraseña_correcta:
        print(" Acceso concedido")
        break
    else:
        print("Acceso denegado")


print("Ingrese un número para ver su tabla de multiplicar:")
numC = int(input())
print("Tabla de multiplicar del " + str(numC) + ":")
for i in range(1, 11):
    print(str(numC) + " x " + str(i) + " = " + str(numC * i))

print("ingrese el area y alrura del rectangulo:")
base = float(input("Base: "))
altura = float(input("Altura: "))
area = calcular_area_del_rectanguulo(base, altura)
print("El área del rectángulo es: ", area)

print("ingrese una cadena de texto:")
cadena = input()
cadena_invertida = cadena_inversa(cadena)
print("La cadena invertida es: ", cadena_invertida)

print("ingrese un número para verificar si es primo:")
numero = int(input())
if es_primo(numero):
    print("El número " + str(numero) + " es primo.")
else:
    print("El número " + str(numero) + " no es primo.")

lista_articulos = ["manzanas", "tacaco", "naranjas", "uvas"]
print(lista_articulos[2])
lista_articulos.append("tacaco IQ")
print(lista_articulos)

lista_promedios = [85.10, 90.6, 78.34, 92.56, 88.4]
promedio_general = sum(lista_promedios) / len(lista_promedios)
print("El promedio general es: ", promedio_general)

lista_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista_duplicados))
print("Lista arreglada: ", lista_sin_duplicados)

print("ingrese una palabra para contar sus vocales:")
palabra = input()
contador_vocales = sum(1 for letra in palabra if letra.lower() in "AEIOUaeiouáéíóú")
print("La palabra '" + palabra + "' tiene " + str(contador_vocales) + " vocales.")

