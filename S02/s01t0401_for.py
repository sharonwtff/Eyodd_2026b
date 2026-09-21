"""
Escribir un programa que calcule la suma de los "n"
 numeros naturales, por ejemplo si  =100, el programa 
calcula la suma de 1 al 100
"""
# importamos bibilioteca time
 
import time

#Creando una marca de tiempo 
timestamp_01 = time.time()

#programa que calcula la suma de los"n"numeros naturales
n = 100
sum= 0
for number in range(1, n + 1):
 print(str(number) + "  ")