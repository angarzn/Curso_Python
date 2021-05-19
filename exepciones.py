def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        if(num <0):
            raise Exception("DEBE INGRESAR UN NUMERO POSITIVO")
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("DEBES INGRESAR UN NÚMERO")
    except Exception as negv:
        print(negv)


if __name__ == '__main__':
    run()