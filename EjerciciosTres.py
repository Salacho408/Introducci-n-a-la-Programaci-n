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

# Ejercicio 3

def simpsonRule(a, b, n):
    k, suma = 0, 0
    if n % 2 != 0:
        ans = "El valor de n debe ser un entero par"
    elif n == 0:
        ans = "El valor de n debe ser diferente de 0"
    else:
        h = ((b-a)/n)
        for k in range(n+1):
            Yk = ((a+k*h)**(3))
            if k != 0 and k != n:
                if k % 2 != 0:
                    suma += ((4)*(Yk))
                else:
                    suma += ((2)*(Yk))
            else:
                suma += Yk
        ans = ((h/3)*(suma))
    return ans

EjercicioTres = simpsonRule(1, 5, 8)
print("Ejercicio tres \n", EjercicioTres, "\n")

# Ejercicio 4

def aproximarEuler(n):
    suma, producto = 1, 1
    for i in range(1, n+1):
        producto *= i
        suma += 1/producto
    ans = suma
    return ans

EjercicioCuatro = aproximarEuler(8)
print("Ejercicio cuatro \n", EjercicioCuatro, "\n")