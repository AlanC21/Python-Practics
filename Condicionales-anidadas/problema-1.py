num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
if num1 > num2:
  if num1 > num3:
    print("El mayor es: ",num1)
  else:
    print("El mayor es: ",num3)
else:
  if num2 > num3:
    print("El mayor es: ",num2)
  else:
    print("El mayor es: ",num3)
