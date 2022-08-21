import random

def run ():
    numero_aleatorio= random.randint(1, 100)
    numero_escogido = int(input("elige un numero: "))
    while numero_escogido != numero_aleatorio:
        if   numero_escogido < numero_aleatorio:
           print ("escoge un numero mas grande: ")
        else:
            print ("escoge un numero mas pequeño: ")
        numero_escogido= int(input("elige otro numero: "))
    print ("ganaste mamawebo")

    pass

if __name__ =="__main__":
    run()