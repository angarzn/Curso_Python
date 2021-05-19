def divisors(num):
        assert num > 0, "Debe ingresar un numero positivo"
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors 


def run():
    num = input('Ingresa un número: ')
    # El método isnumeric devuelve true si el string ingresado ...
    # corresponde a caracteres numéricos, en caso contrario devulve false
    assert num.replace("-","").isnumeric(), "Debe ingresar un numero"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()