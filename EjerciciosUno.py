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

EjercicioTres = sumarMayorMenor(8, 7, 3, 4, 2)
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

EjercicioCinco = cuantosEnCuadrante(8, 7, 3, 4, 2, 3, 8, 7, 3)
print("Ejercicio cinco \n", EjercicioCinco, "\n")