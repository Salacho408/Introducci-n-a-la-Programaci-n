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

# Ejercicio 2

def leerNumeros():
    salida = True
    cantidadDatos, cantidadImpares, sumaMultiplosCinco, cantidadMayoresDiezMenoresVeinte = 0, 0, 0, 0
    tuplaNumeros = ()
    while salida == True:
        dato = input(" Numero: ")
        if dato != "Fin":
            datoEntero = int(dato)
            cantidadDatos += 1
            if (datoEntero % 2 != 0):
                cantidadImpares += 1
            if (datoEntero % 5 == 0):
                sumaMultiplosCinco += datoEntero
            if (datoEntero > 10 and datoEntero < 20):
                cantidadMayoresDiezMenoresVeinte += 1
        else:
            salida = False
    tuplaNumeros = tuplaNumeros + (cantidadDatos, cantidadImpares, sumaMultiplosCinco, cantidadMayoresDiezMenoresVeinte)
    print("", tuplaNumeros)
    
print("Ejercicio dos")
leerNumeros()
print("\n")

# Ejercicio 3

def imprimirPotencias(n, m):
    potencia = 0
    if (n != 0) and (n != 1):
        while (n**potencia) <= m:
            print("", n**potencia)
            potencia += 1
    else:
        if n == 1:
            if m != 0:
                print("", 1)
        else:
            print("", 0)

def leerImprimir():
    numeroEjecuciones = int(input(" Numero de ejecuciones del programa: "))
    for _ in range(numeroEjecuciones):
        numeroUno = int(input(" Primer numero: "))
        numeroDos = int(input(" Segundo numero: "))
        imprimirPotencias(numeroUno, numeroDos)

print("Ejercicio tres")
leerImprimir()
print("\n")

# Ejercicio 4

def calcularSueldo(sal, e, n):
    sumatoria = 0
    for i in range(1, (n+1)):
        sumatoria += i
    total = sal + (e * 10000) + (sumatoria * 5000)
    return total

def leerImprimir():
    numeroEjecuciones = int(input(" Numero de ejecuciones del programa: "))
    for _ in range(numeroEjecuciones):
        datoUno = int(input(" Salario base: "))
        datoDos = int(input(" Edad del empleado: "))
        datoTres = int(input(" Años en la compañia: "))
        ans = calcularSueldo(datoUno, datoDos, datoTres)
        print("", ans)

print("Ejercicio cuatro")
leerImprimir()
print("\n")

# Ejercicio 5

def Hajj_e_Akbar():
    salida = True
    tuplaDatos = ()
    while salida == True:
        dato = input(" Peregrinacion: ")
        if dato != "*":
            tuplaDatos = tuplaDatos + (dato,)
        else:
            salida = False
    for i in range(len(tuplaDatos)):
        if tuplaDatos[i] == "Hajj":
            print(" Case", (i+1), ": Hajj-e-Akbar")
        else:
            print(" Case", (i+1), ": Hajj-e-Asghar")    

print("Ejercicio cinco")
Hajj_e_Akbar()