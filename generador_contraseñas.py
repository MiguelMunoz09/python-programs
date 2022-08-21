import random

def generar_contrasena():
    mayusculas = [ "A", "B", "C", "D","E", "F", "G", "H", 
    "I" ]
    minisculas = ["a", "b", "c","d","e","f","g", "h", "i"]
    simbolos = ["!", "#", "$","&","/","*","+"]
    numeros= ["1","2","3", "4","5","6","7","8","9","10"]

    caracteres= mayusculas + minisculas + simbolos + numeros
    contrasena= []

    for i in range (20):
        contrasena_random = random.choice(caracteres)
        contrasena.append(contrasena_random)

    contrasena="".join(contrasena)
    return contrasena



def run ():
    contrasena = generar_contrasena()
    print (" tu nueva contrasena es: " + contrasena)


if __name__=="__main__":
    run()