nPersonas = int(input("Ingrese la cantidad de personas: "))
i=1
sumaTotal = 0
while i <= nPersonas:
    altura = float(input("Ingrese la altura de la persona: "))
    sumaTotal = sumaTotal + altura
    i = i + 1
promedio = sumaTotal / nPersonas
print("Promedio de altura de las personas: ", promedio)