import time
n=100
thesum=0
timestamp_01 = time.time()
#iniciando la suma n=100

while (n>0):
    thesum = thesum + n #100 +99 + 98+...+1
    n =  n - 1
    #tomams el t2
    timestamp_02 = time.time()
    #imprimimos la solucion
   
print(f"la suma es: {thesum}")

#calculamos el tiempo de ejecucion
elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
print(f"Tiempo de ejecucion: {elapsed_time} microsegundos")
