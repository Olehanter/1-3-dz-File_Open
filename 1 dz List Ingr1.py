import pprint
import os

with open(r'C:\Users\Администратор\PycharmProjects\pythonProject6\recipes.txt') as f:
    cook_book = []

    for line in f:
        cook_name = line.strip()
        counts = int(f.readline())
        emcount = []
        for i in range(counts):
            emco = f.readline().strip()
            name, lot, unit = emco.split(' | ')
            emcount.append({
                'Название ингредиента': name,
                'Количество ': lot,
                'Единица измерения': unit
            })
        f.readline()
        cook_book.append({
            ' Название блюда': cook_name,
            'Количество ингридиентов в блюде': emcount
        })

        pp = pprint.PrettyPrinter(sort_dicts=False)
        pp.pprint(cook_book)
