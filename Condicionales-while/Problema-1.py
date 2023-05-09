nAlumnos = int(input("Ingrese número de alumnos: "))
i=1
cant=0
while i <= nAlumnos:
    nota = float(input("Ingrese la nota del alumno: "))
    if nota >= 7:
        cant = cant + 1
    i = i + 1
print("Cantidad de alumnos con nota mayor o igual a 7: ", cant)
