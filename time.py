import time
import sys 


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial_r(n-1)

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
        
    return respuesta


if __name__ == '__main__':

    sys.setrecursionlimit(20000)
    n = 1000
    
    comienzo = time.time() # Tiempo antes de iniciar el método factorial
    print(f'tiempo inicio: {comienzo}')
    factorial(n)
    final = time.time() # Tiempo tras terminar el método factorial
    print(f'tiempo final: {final}')
    print(f'Tiempo factorial interativo : {final - comienzo}') # Duración del metodo factorial 


    comienzo1= time.time() # Tiempo antes de iniciar el método factorial recursivo
    print(f'tiempo inicio: {comienzo1}')
    print(factorial_r(n))
    final1 = time.time() # Tiempo tras terminar el método factorial recursivo
    print(f'tiempo final: {final1}')
    print(f'Tiemp factorial recursivo : {final1 - comienzo1}') # Duración del metodo factorial recursivo
