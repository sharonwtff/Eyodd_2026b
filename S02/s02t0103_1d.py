# archivo
from array import array as arr

from s02t0102_1d import print_array
my_array = arr('i',[2,10,15,20])

print("antes de la eliminacion ")
print_array(my_array)

#eliminacion

try:
   my_array.remove(100)
except:
   print("no se encuentra este numero en el arreglo")
 

print("despues de la eliminacion")
print_array(my_array)

# print(f"arreglo antes de la insercion:")
# print_array(my_array)

# #insercion
# my_array.insert(1, 90)

# print("arreglo despues de la insercion:")
# print_array(my_array)

# print("Simular un appedn con insert")
# my_array.insert(len(my_array), 90000)
# print_array(my_array)