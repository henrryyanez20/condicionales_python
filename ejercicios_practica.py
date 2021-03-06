#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''

    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el segundo número:\n'))
    diferencia = numero_1 - numero_2

    if diferencia < 0:
        print("Resultado NEGATIVO")
    elif diferencia == 0:
        print("Resultado igual a CERO")
    else:
        print("Resultado POSITIVO")        


def ej2():
# Ejercicios de práctica con números

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
  '''
  numero_1 = int(input('Ingrese el primer número:\n'))
    
  if (numero_1 % 2) == 0:
    print("Numero 1 es PAR")
  else:
    print("Numero 1 es IMPAR")

  numero_2 = int(input('Ingrese el segundo número:\n'))

  if (numero_2 % 2) == 0:
    print("Numero 2 es PAR")
  else:
    print("Numero 2 es IMPAR")

  numero_3 = int(input('Ingrese el tercer número:\n'))

  if (numero_3 % 2) == 0:
    print("Numero 3 es PAR")
  else:
    print("Numero 3 es IMPAR")

def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)
    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    
    '''

    numero_1 = int(input('Ingrese el primer número:\n'))
    numero_2 = int(input('Ingrese el segundo número:\n'))
    operacion = input('''Ingrese el simbola de la operacion a realizar :\n
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**) \n''')

    if operacion == "+":
      print("La SUMA de {} + {} es : ".format(numero_1,numero_2), numero_1+numero_2)
    elif operacion == "-":
      print("La RESTA de {} - {} es : ".format(numero_1,numero_2), numero_1-numero_2)
    elif operacion == "*":
      print("La MULTIPLICACION de {} * {} es : ".format(numero_1,numero_2), numero_1*numero_2)
    elif operacion == "/":
      print("La DIVISION de {} / {} es : ".format(numero_1,numero_2), numero_1/numero_2)
    else:
      print("La POTENCIA de {} elevado a {} es : ".format(numero_1,numero_2), numero_1**numero_2)

def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor
    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palabra_1 = str(input('Ingrese la primera palabra:\n'))
    palabra_2 = str(input('Ingrese la segunda palabra:\n'))
    palabra_3 = str(input('Ingrese la tercera palabra:\n'))

    print('''
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra) \n''')

    opcion = int(input('Ingrese la opción 1 o 2 según su necesidad:\n'))

    if opcion == 1:
      if (palabra_1 < palabra_2 < palabra_3):
        print(palabra_1,palabra_2,palabra_3)
      elif (palabra_1 > palabra_2 > palabra_3):
        print(palabra_3,palabra_2,palabra_1)

    else:
      a = len(palabra_1)
      b = len(palabra_2)
      c = len(palabra_3)

      #TENGO DUDAS COMO HACERLO CON TRES PALABRAS

def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?
    En cada caso imprimir en pantalla el resultado  
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
    #ej5()
