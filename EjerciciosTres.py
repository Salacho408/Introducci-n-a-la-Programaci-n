# Santiago Salazar Gil
import math

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
    for i in range(1, (n+1)):
        producto *= i
        suma += (1/producto)
    ans = suma
    return ans

EjercicioCuatro = aproximarEuler(8)
print("Ejercicio cuatro \n", EjercicioCuatro, "\n")

# Ejercicio 5

def imprimirLineasNumeros(n):
    numero, nAux = n, n
    for _ in range(n):
        print(" ", end = "")
        for i in range(nAux):  
            if i != (nAux-1):
                print(numero, "", end = "")
            else:
                print(numero)
                ultimoNumero = (numero - 1)
                numero = ((nAux * 2) + ultimoNumero)
            numero -= 1
        nAux -= 1
        
print("Ejercicio cinco")
imprimirLineasNumeros(3)
print("\n")

# Ejercicio 6

def filtrarValoresEnPosicion(l):
    ans = []
    for i in range(len(l)):
        if i == l[i]:
            ans.append(i)
    return ans

EjercicioSeis = filtrarValoresEnPosicion([10, 8, 4, 6, 15, 12, 2, 19])
print("Ejercicio seis \n", EjercicioSeis, "\n")

# Ejercicio 7

def reemplazar(l, v1, v2):
    for i in range(len(l)):
        if l[i] == v1:
            l[i] = v2
    ans = l
    return ans

EjercicioSiete = reemplazar([4, 1, 11, 1, 8, 1, 1, 5, 6, 7, 17, 1], 1, 100)
print("Ejercicio siete \n", EjercicioSiete, "\n")

# Ejercicio 8

def perimetroFigura(listaUno, listaDos):
    ans = 0
    tamanio = len(listaUno)
    if len(listaUno) != len(listaDos):
        ans = "Las listas deben tener el mismo tamaño"
    else:
        if tamanio < 3:
            ans = "No existen poligonos con menos de tres lados"
        else:
            for i in range(tamanio):
                x1 = listaUno[i]
                y1 = listaDos[i]
                if i != (tamanio-1):
                    x2 = listaUno[i+1]
                    y2 = listaDos[i+1]
                else:
                    x2 = listaUno[0]
                    y2 = listaDos[0]
                ans += math.sqrt(((x2-x1)**(2)) + ((y2-y1)**(2)))
    return ans

EjercicioOcho = perimetroFigura([8, 7, 3], [4, 2, 3])
print("Ejercicio ocho \n", EjercicioOcho, "\n")

# Ejercicio 9 (sacarFactorial incluye al 0, a pesar de que factAcumInv no tiene en cuenta el factorial de 0)

def sacarFactorial(n):
    factorial = n
    i = (n-1)
    if n != 0:
        while i > 1:
            factorial *= i
            i -= 1
    else:
        factorial = 1
    return factorial

def factAcumInv(N):
    ans = []
    while N >= 1:
        numero = sacarFactorial(N)
        ans.append(numero)
        N -= 1
    return ans

EjercicioNueve = factAcumInv(7)
print("Ejercicio nueve \n", EjercicioNueve, "\n")    

# Ejercicio 10 (Asumiendo que las razones menores que 0 y mayores que 99 no alteran el valor de sumatoriaNumeros)

def Emoogle_Balance():
    salida = True
    listaDiferencias = []
    i = 0
    while salida == True:
        numeros = []
        sumatoriaNumeros, sumatoriaCeros = 0, 0
        if i != 75:
            numeroEnteros = int(input(" Numero de enteros: "))
        if numeroEnteros < 0 or numeroEnteros > 1000:
            listaDiferencias.append("El numero de enteros debe ser un valor situado entre 1 y 1000")
        else:
            if numeroEnteros != 0 and i != 75:
                print(" Enteros: ", end = "")                
                numeros = input().split()
                for j in range(len(numeros)):
                    numeros[j] = int(numeros[j])                 
                for j in range(len(numeros)):
                    if numeros[j] == 0:
                        sumatoriaCeros += 1
                    else:
                        if numeros[j] >= 1 and numeros[j] <= 99:
                            sumatoriaNumeros += 1
                if len(numeros) != numeroEnteros:
                    listaDiferencias.append("Cantidad erronea de enteros ingresados")
                else:
                    diferencia = sumatoriaNumeros - sumatoriaCeros
                    listaDiferencias.append(diferencia)
                i += 1
            else:
                salida = False    
    for i in range(len(listaDiferencias)):
        print(" Case", (i+1), ":", listaDiferencias[i])

print("Ejercicio diez")
Emoogle_Balance()
print("\n")     