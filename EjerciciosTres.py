# Santiago Salazar Gil

# Ejercicio 1

def imprimirSucesion(n):
    for i in range(1, (n+1)):
        valorSucesion = ((-1/i)**(i))
        if i != n:
            print(" %.4f," % valorSucesion, end = "")
        else:
            print(" %.4f" % valorSucesion)
        
print("Ejercicio uno")
imprimirSucesion(5)
print("\n")

# Ejercicio 2

def formarTriangulo(x, y):
    for _ in range(y):
        print(" ", end = "")
    for _ in range((x*2)-1):
        print("*", end = "")
    print("")

def imprimirAsteriscos(n):
    salida, flag = True, True
    valorAux = 1
    numEspacios = (n*2)-1
    while salida == True and n != 0:
        if valorAux != n and flag == True:
            formarTriangulo(valorAux, numEspacios)
            valorAux += 1
            numEspacios -= 2
        else:
            flag = False
            formarTriangulo(valorAux, numEspacios)
            valorAux -= 1
            numEspacios += 2
        if valorAux < 1:
            salida = False

print("Ejercicio dos")
imprimirAsteriscos(3)
print("\n")