n = int(input("Ingrese la cantidad de triangulos: "))
cantEquilateros = 0
cantIsosceles = 0
cantEscalenos = 0
for x in range(n):
    lado1 = int(input("Ingrese el lado 1: "))
    lado2 = int(input("Ingrese el lado 2: "))
    lado3 = int(input("Ingrese el lado 3: "))
    if(lado1 == lado2 and lado1 == lado3):
        print("Es un Triangulo Equilateros")
        cantEquilateros =+ 1
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("Es un Triangulo Isosceles")
        cantIsosceles =+ 1
    else:
        print("Es un Triangulo Escalenos")
        cantEscalenos =+ 1
print("La cantidad de Triangulos Equilateros son: ", cantEquilateros, "\nLa cantidad de Triangulos Isosceles son: ", cantIsosceles, "\nLa cantidad de Triangulos Escalenos son: ", cantEquilateros)



