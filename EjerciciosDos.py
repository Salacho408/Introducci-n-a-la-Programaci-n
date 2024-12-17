# Santiago Salazar Gil

# Ejercicio 1

def imprimirNumerosFor():
    for i in range(1, 1001):
        if (900 % i == 0) or (i % 13 == 0):
            print(" ", i)

def imprimirNumerosWhile():
    i = 1
    while i < 1001:
        if (900 % i == 0) or (i % 13 == 0):
            print(" ", i)
        i += 1

print("Ejercicio uno \n", "Usando ciclos for: ")
imprimirNumerosFor()
print(" Usando ciclos while: ")
imprimirNumerosWhile()
print("\n")