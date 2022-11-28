# Ejemplo de condicion anidada elif

print("Ingrese un primer numero")
numero1 = float(input())
print("Ingrese un segundo numero")
numero2 = float(input())
print("Ingrese un tercer numero")
numero3 = float(input())

if numero1 < numero2 and numero1 < numero3:
    print ("Numero 1 es el menor de todos")
elif numero2 < numero3:
    print("Numero 2 es el menor de todos")
else:
    print("Numero 3 es el menor de todos")