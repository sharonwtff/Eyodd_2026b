# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack','Alejandro','Oscar'] # O(1)

def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)
    

    for student in students:
        print("Se le suma 1 al total")
        total += 1 # O(n) es n por el numero de estudiantes en la lista
        new_list.append(student) # O(n) por que se ejecuta tantas veces tenga la lista

    print(new_list) # O(1)
    return total # O(1)

print(random_function(student_list_01))
print(f"Tamaño de lista {len(student_list_01)}")
print(random_function(student_list_01))

# ⭐Calcular O(2n)+O(5) = O(2n+5)=O(n)⭐


#🥗EXPLICACIÓN DE COMPLEJIDAD:🥗

#🍎 student_list_01 → O(1)
#Crear y asignar la lista es una operación constante.
#
#🍎 first = students[0] → O(1)
#Acceder directamente al primer elemento es una operación constante.
#
#🍎 total = 0 → O(1)
#Asignar un valor a una variable es una operación constante.
#
#🍎 new_list = [] → O(1)
#Crear una lista vacía es una operación constante.
#
#🍌 for student in students → O(n)
#El for recorre todos los elementos de la lista.
#Si hay n estudiantes, se repite n veces.
#
#🍌 total += 1 → O(n)
#La suma es O(1), pero como está dentro del for se realiza n veces.
#
#🍌 new_list.append(student) → O(n)
#append() es O(1), pero se ejecuta n veces dentro del for.
#
#🍉 print(new_list) → O(n)
#Se imprime una lista que contiene n elementos, por eso es O(n).
#
#🍉 return total → O(1)
#Regresar el valor de total es una operación constante.
#
#🍇 print(f"Tamaño de la lista {len(student_list_01)}") → O(1)
#len() obtiene el tamaño de la lista en tiempo constante.
#
#🍓 RESULTADO FINAL 🍓
#O(1) + O(1) + O(1) + O(n) + O(n) + O(n) + O(1)
#
#🍓 = O(3n + 4)
#
#🍓 Eliminamos las constantes:
#O(3n + 4) = O(n)
#
#🍑 NOTA SOBRE LOS FOR 🍑
#🍑 El for no significa automáticamente O(1).
#Se debe revisar cuántas veces se ejecuta su contenido.
#
#🍑 Si hay 4 estudiantes, el ciclo se repite 4 veces.
#🍑 Si hay 100 estudiantes, el ciclo se repite 100 veces.
#🍑 Por eso en este caso tenemos O(n).
#
#🥝 NOTA SOBRE FOR ANIDADOS 🥝
#🥝 Si colocamos un for dentro de otro for, las repeticiones se multiplican.
#🥝 O(n) × O(n) = O(n²)
#
#🥭 REGLA PARA RECORDAR 🥭
#🥭 Una operación que ocurre una sola vez → O(1)
#🥭 Un for que recorre n elementos → O(n)
#🥭 Dos for anidados → O(n²)
#
#🍓 COMPLEJIDAD FINAL: O(n) 🍓
#🍓 La función crece de manera proporcional a la cantidad de estudiantes.
