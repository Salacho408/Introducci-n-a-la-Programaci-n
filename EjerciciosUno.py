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
print(" Volumen del cono: ", EjercicioDosCono, "\n", "Volumen de la esfera: ", EjercicioDosEsfera)