cantPT=int(input("Ingrese la cantidad de preguntas: "))
cantRC=int(input("Ingrese la cantidad de respuestas correctas: "))
promedio=cantRC/cantPT
if promedio >= 0.9:
  print("Nivel maximo")
else:
  if promedio >= 0.75:
    print("Nivel medio")
  else:
    if promedio >= 0.5:
      print("Nivel regular")
    else:
      print("Fuera de nivel")