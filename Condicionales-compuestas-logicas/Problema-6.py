sueldo = int(input("Ingrese sueldo:"))
antiguedad = int(input("Ingrese antigüedad:"))
if sueldo < 500 and antiguedad >= 10:
    print("Sueldo final:", sueldo*0.2)
elif sueldo < 500 and antiguedad < 10:
    print("Sueldo final:", sueldo*0.05)
else:
    print("Sueldo final:", sueldo)
    