def get_shop_list_by_dishes(dishes, person_count):
    with open(r'C:\Users\Администратор\PycharmProjects\pythonProject6\recipes.txt') as f:
        cook_book = {}
        for line in f:
            l_name = line.strip()
            count_ = int(f.readline())
            ingredients = []
            for i in range(count_):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })

            f.readline()
            cook_book[l_name] = ingredients

    l_dishes = {}
    for _dish in dishes:
        if _dish in cook_book.keys():
            for _ingredients in cook_book[_dish]:
                elem = _ingredients['ingredient_name']
                if elem in l_dishes.keys():
                    l_dishes[elem]['quantity'] += int(_ingredients['quantity']) * person_count
                else:
                    alt = _ingredients['measure']
                    l_dishes[elem] = {'quantity': int(_ingredients['quantity']) * person_count,
                                      'measure': alt}

    return (l_dishes)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4))
