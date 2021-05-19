DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Filtrando con list comprehensions aquellos trabajadores que manejen el lenguaje Python
    Python_dev = [worker["name"] for worker in DATA if worker["language"] == "python"]


    # Filtrando con list comprehensions aquellos trabajadores de Platzi
    Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]


    # Filtrando con filter()  aquellos trabajores mayores de edad
    Adult_workers = list(filter(lambda worker: worker["age"] > 18, DATA))
    Adult_workers = list(map(lambda worker:worker["name"], Adult_workers))


    # Creación de una nueva llave en los diccionarios de DATA, true para aquellos mayores de 70
    old = list(map(lambda worker:worker | {"old": worker["age"] > 70}, DATA))
    # Para concatenar diccionarios se usa el pipe operator 
    for i in old:
       print(i)


if __name__ == "__main__":
    run()