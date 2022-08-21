# pesos = input("inserte la cantidad de pesos a convertir: ")
# pesos =float(pesos)
# valor_dolar =3875 
# dolares=pesos/valor_dolar
# dolares=round(dolares, 2)
# dolares=str(dolares)
# print("tienes $" + dolares + " dolares")


# dolares = input("ingrese la cantidad de dolares: ")
# dolares= float(dolares)
# valor = 0.26
# pesos = dolares / valor
# pesos=round (pesos, 2)
# pesos=str (pesos)
# print("tienes $" + pesos + " pesos")


from pickletools import OpcodeInfo
from tkinter import Menu



def funcion(valor_dolar):
    pesos = input("inserte la cantidad de pesos a convertir: ")
    pesos = float(pesos) 
    dolares= pesos/valor_dolar
    dolares=round(dolares, 2)
    dolares=str(dolares)
    print("tienes $" + dolares + " dolares")

Menu= """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

Elige una opcion: """

Opcion = int(input(Menu))

if Opcion == 1:
   funcion(3875)

elif Opcion== 2:
    funcion(108.79)

elif Opcion== 3:
    funcion(20.92)
else:
    print("mamawebo inserta bien esa mielda")

# poner siempre el equivalente de un dolar en cualquier moneda.



