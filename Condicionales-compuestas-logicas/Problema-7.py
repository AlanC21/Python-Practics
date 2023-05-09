num1 = int(input("Ingrese primer número:"))
num2 = int(input("Ingrese segundo número:"))
num3 = int(input("Ingrese tercer número:"))
if num1 < num2 and num1 < num3:
    print(num1);
elif num2 < num3:
    print(num2);
else:
    print(num3);
if num1 > num2 and num1 > num3:
    print(num1);
elif num2 > num3:
    print(num2);
else:
    print(num3);
