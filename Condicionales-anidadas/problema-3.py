num=int(input("Ingrese un numero: "))
if num < 10:
    print("El numero tiene un digito")
else:
  if num < 100:
    print("El numero tiene dos digitos")
  else:
    if num < 1000:
      print("El numero tiene tres digitos")
    else:
      print("ERROR: El numero tiene mas de tres digitos")

