
"""
Notas:
1.identifico el tamaño de   la entrada"n"
El tamaño de la entrada es el numero de estudiantes 
2. Es ver  cuanto crece el numero el tamaño de de la entrada
Agrego las bigO identicas 
Teniendo en cuenta la Cota superior asintótica
O(n) + O(4)=O(n+4) = O(n)
"""


# Creando una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Sharck']
student_list_02 = ['Mike','Saul','Walter','Jessy']

#Verificando presencia de estudiante
def check_student(input_student,student_list):
    for student in student_list:
        if student == student:
            print ("Estudiante encontrado")
            return student #O(1)
        #Si no encuentro al estudiante 
        print("Estudiante no esta encontrado")
        return None

 #Probando algoritmo 
check_student("Walter",student_list_01)   