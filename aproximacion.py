def run():
    from time import time
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2 
    respuesta = 0.0
    tiempo_inicio = time()
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
        
    tiempo_total = time() - tiempo_inicio

    if abs(respuesta**2 - objetivo) >= epsilon:
        print("No se encontro la raiz cuadrada" + objetivo)
        print(f'Tardo {tiempo_total} segundos')
    else:
        print("La raiz cudrada de" + str(objetivo) + "es" + str(respuesta))
        print(f'Tardo {tiempo_total} segundos')
    
if __name__=="__main__":
        run()