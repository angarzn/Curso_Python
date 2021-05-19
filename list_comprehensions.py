def run():
    # squares = []

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # List comprehensions para hacer una lista con el cuadrado de los número del 1 al 100
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # List comprehension para hacer lista con los números de 1 a 99999 divisibles por 4, 6 y 9
    reto = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(reto)

    
if __name__ == "__main__":
    run()