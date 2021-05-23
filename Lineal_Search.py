import random

def lineal_search(lista, objetivo):
    match = False
    for elemento in lista: #  O(n) crece de forma lineal
        if elemento == objetivo:
            match = True
            break
    return match        

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = lineal_search(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
