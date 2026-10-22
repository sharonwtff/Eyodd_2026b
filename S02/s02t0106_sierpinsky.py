from array import array as arr

#Parametros de mi cuadricula.
rows = 8
columns = 2 * rows - 1

#Creando el Grid 2D.
matrix = []
#Construyendo el Grid.
for _ in range(rows):
    new_rows = arr('i', [0] * columns)
    matrix.append(new_rows)

#Validando la construccion del Grid.
print(f"Cantidad de filas: {len(matrix)}")
print(f"Cantidad de columnas: {len(matrix[0])}")

for rows in matrix:
    print(list(rows))