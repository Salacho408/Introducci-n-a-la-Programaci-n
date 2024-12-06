# Santiago Salazar Gil
import math

# Ejercicio 1

def calcularFuncion(x, z, y, w):
    varUno = (((x-2)**(z+1))*((4*y)**(4*z)))
    varDos = ((7)*((x)**(y-1)))
    varTres = ((math.sqrt(x+3))/(4))
    varCuatro = (((z)**(4))*((w)**(y+x))*((x)**(3)))
    varCinco = 6
    ans = (varUno + varDos - varTres - varCuatro + varCinco)
    return ans

EjercicioUno = calcularFuncion(8, 7, 3, 4)
print("Ejercicio uno \n", EjercicioUno, "\n")

# Ejercicio 2

def calcularCilindro(r, h):
    volumenCilindro = ((math.pi)*((r)**(2))*(h))
    return volumenCilindro

def calcularCono(r, h):
    volumenCono = ((1/3)*(math.pi)*((r)**(2))*(h)) 
    return volumenCono

def calcularEsfera(r):
    volumenEsfera = ((4/3)*(math.pi)*((r)**(3)))
    return volumenEsfera

EjercicioDosCilindro = calcularCilindro(8, 7)
EjercicioDosCono = calcularCono(3, 4)
EjercicioDosEsfera = calcularEsfera(2)
print("Ejercicio dos \n", "Volumen del cilindro: ", EjercicioDosCilindro)
print(" Volumen del cono: ", EjercicioDosCono, "\n", "Volumen de la esfera: ", EjercicioDosEsfera, "\n")

# Ejercicio 3

def sumarMayorMenor(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        numMayor = a
    elif b > a and b > c and b > d and b > e:
        numMayor = b
    elif c > a and c > b and c > d and c > e:
        numMayor = c
    elif d > a and d > b and d > c and d > e:
        numMayor = d
    else:
        numMayor = e
    if a < b and a < c and a < d and a < e:
        numMenor = a
    elif b < a and b < c and b < d and b < e:
        numMenor = b
    elif c < a and c < b and c < d and c < e:
        numMenor = c
    elif d < a and d < b and d < c and d < e:
        numMenor = d
    else:
        numMenor = e
    ans = (numMayor + numMenor)
    return ans

EjercicioTres = sumarMayorMenor(6, 1, 7, 2, 3)
print("Ejercicio tres \n", EjercicioTres, "\n")

# Ejercicio 4

def determinarCuadrante(x, y):
    if x > 0 and y > 0:
        ans = 1
    elif x < 0 and y > 0:
        ans = 2
    elif x < 0 and y < 0:
        ans = 3
    else:
        ans = 4
    return ans

EjercicioCuatro = determinarCuadrante(8, 7)
print("Ejercicio cuatro \n", EjercicioCuatro, "\n")

# Ejercicio 5

def sumarEnCuadrante(punto, cuadrante):
    if punto == cuadrante:
        suma = 1
    else:
        suma = 0
    return suma
    
def cuantosEnCuadrante(x1, y1, x2, y2, x3, y3, x4, y4, c):
    ans = 0
    primerPunto = determinarCuadrante(x1, y1)
    ans += sumarEnCuadrante(primerPunto, c)
    segundoPunto = determinarCuadrante(x2, y2)
    ans += sumarEnCuadrante(segundoPunto, c)
    tercerPunto = determinarCuadrante(x3, y3)
    ans += sumarEnCuadrante(tercerPunto, c)
    cuartoPunto = determinarCuadrante(x4, y4)
    ans += sumarEnCuadrante(cuartoPunto, c)
    return ans

EjercicioCinco = cuantosEnCuadrante(2, 3.4, 3, 1, -2.1, -3, -4, 1, 1)
print("Ejercicio cinco \n", EjercicioCinco, "\n")

# Ejercicio 6

def compararCartas(a, b, c, d, e):
    cantidad = 1
    if a == b:
        cantidad += 1
    if a == c:
        cantidad += 1
    if a == d:
        cantidad += 1
    if a == e: 
        cantidad += 1
    return cantidad

def tienePoquer(cartaUno, cartaDos, cartaTres, cartaCuatro, cartaCinco):
    c1 = compararCartas(cartaUno, cartaDos, cartaTres, cartaCuatro, cartaCinco)
    c2 = compararCartas(cartaDos, cartaUno, cartaTres, cartaCuatro, cartaCinco)
    c3 = compararCartas(cartaTres, cartaUno, cartaDos, cartaCuatro, cartaCinco)
    c4 = compararCartas(cartaCuatro, cartaUno, cartaDos, cartaTres, cartaCinco)
    c5 = compararCartas(cartaCinco, cartaUno, cartaDos, cartaTres, cartaCuatro)
    if c1 == 4 or c2 == 4 or c3 == 4 or c4 == 4 or c5 == 4:
        ans = True
    else:
        ans = False
    return ans

EjercicioSeis = tienePoquer("A", "2", "2", "2", "Q")
print("Ejercicio seis \n", EjercicioSeis, "\n")

# Ejercicio 7

def ganadorSet(pJ1, pJ2):
    if ((pJ1 == 6) and (pJ2 <= (pJ1 - 2))) or ((pJ1 == 7) and ((pJ2 == 5) or (pJ2 == 6))):
        j1 = 1
        j2 = 0
    elif ((pJ2 == 6) and (pJ1 <= (pJ2 - 2))) or ((pJ2 == 7) and ((pJ1 == 5) or (pJ1 == 6))):
        j1 = 0
        j2 = 1
    else:
        j1 = 0
        j2 = 0
    return j1, j2

def ganaPartido(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, jugadorUno, jugadorDos):
    resultadoJ1 = 0
    resultadoJ2 = 0
    contrincanteUno, contrincanteDos = ganadorSet(p1, p2)
    resultadoJ1 += contrincanteUno
    resultadoJ2 += contrincanteDos
    contrincanteUno, contrincanteDos = ganadorSet(p3, p4)
    resultadoJ1 += contrincanteUno
    resultadoJ2 += contrincanteDos
    contrincanteUno, contrincanteDos = ganadorSet(p5, p6)
    resultadoJ1 += contrincanteUno
    resultadoJ2 += contrincanteDos
    contrincanteUno, contrincanteDos = ganadorSet(p7, p8)
    resultadoJ1 += contrincanteUno
    resultadoJ2 += contrincanteDos
    contrincanteUno, contrincanteDos = ganadorSet(p9, p10)
    resultadoJ1 += contrincanteUno
    resultadoJ2 += contrincanteDos
    if resultadoJ1 > resultadoJ2:
        ans = jugadorUno
    else:
        ans = jugadorDos
    return ans

EjercicioSiete = ganaPartido(6, 4, 7, 5, 3, 3, 2, 6, 7, 6, "Santiago", "Carlos")
print("Ejercicio siete \n", EjercicioSiete, "\n")

# Ejercicio 8

def puedeAlmorzar(proteina, numCalorias, pesoAlmuerzo, pesoEnsalada):
    if proteina == "Carne desmechada":
        almuerzo = "Almuerzo permitido"
    elif numCalorias < 500:
        almuerzo = "Almuerzo permitido"
    elif ((numCalorias >= 500) and (numCalorias < 700)) and ((pesoAlmuerzo < 325) and (pesoEnsalada >= 100)):
        almuerzo = "Almuerzo permitido"
    elif pesoEnsalada > (pesoAlmuerzo * 0.60):
        almuerzo = "Almuerzo permitido"
    else:
        almuerzo = "Almuerzo no permitido"
    return almuerzo

EjercicioOcho = puedeAlmorzar("Carne desmechada", 600, 300, 150)
print("Ejercicio ocho \n", EjercicioOcho, "\n")

# Ejercicio 9

def puedeAtacar(filaReina, columnaReina, filaPeon, columnaPeon):
    if (filaReina == filaPeon) or (columnaReina == columnaPeon):
        ans = "Puede atacar"
    elif abs(filaReina - filaPeon) == abs(columnaReina - columnaPeon):
        ans = "Puede atacar"
    else:
        ans = "No puede atacar"
    return ans

EjercicioNueve = puedeAtacar(8, 7, 3, 4)
print("Ejercicio nueve \n", EjercicioNueve, "\n")