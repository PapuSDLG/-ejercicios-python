contador = 0
numero = int(input("Escriba un numero: "))
for i in range(1, numero+1):
    if (numero % i == 0):
        contador += 1
if contador == 2:
    print("Es primo")
else:
    print("No es primo")