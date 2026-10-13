import array as arr

#creacion de un arreglo 
# 1: entero con signo 
# i: entero sin signo
# f: Numero de decimal
# d; numero decimal doble
# u ; Caracteres unicode
my_array = arr.array('i',[111,222,333,444,555,666,777,888,999,1010])

#iteracion automatica


# for num in my_array:
#     print(num)

#acesso individual a los elementos del arreglo

# print(my_array[0] )
# print(my_array[1] )
# print(my_array[2] )

#tamaño de un arreglo 
#len

# print(len(my_array))    
    
#iteracion por indices
# for i in range(len(my_array)):
    # print(f"Elemento en el indice {i+1} es: {my_array[i]}")
  #  if my_array[i] %2 == 0:
    #  print(f"elemento num{i+1}:{my_array[i]}")

#Busqueda de un elemento de un arreglo
num_to_search = 200

try:
  print(f"Location {num_to_search}: {my_array.index(num_to_search)}")
except :
  print(" ⚠️ Numero no encontrado ❌!!!")