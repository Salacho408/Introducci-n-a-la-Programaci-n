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
print("Ejercicio uno \n", EjercicioUno)