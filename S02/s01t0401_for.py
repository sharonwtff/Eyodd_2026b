"""
Escribir un programa que calcule la suma de los "n"
numeros naturales, por ejemplo si n = 100, el programa 
calcula la suma de 1 al 100
"""
# importamos bibilioteca time

import time

#funcion que suma los primeros n numeros naturales
def sum_of_n(n):
    total_sum = 0
    #sumando los n numeros
    #ciclo for
    for number in range(1, n + 1):
        total_sum += number
    #retornando la suma total
    return total_sum

#VARIABLE PARA GUARDAR
#El data set
dataset = []

#generando el contenido del datset
for repetition in range(1, 11):
    #Creando una marca de tiempo 
    timestamp_01 = time.time()
    #sumo los n numeros

    n = repetition * 500
    #guardo el resultado       
    result = sum_of_n(n)

    timestamp_02 = time.time()
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2) 
    #agregar la tripleta de los datos al dataset
    dataset.append((n, elapsed_time, result))

#imprimir el dataset
for tup in dataset:
    print(tup)
