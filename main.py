from pprint import pprint

def read_recipes_from_file():
    cook_book_file = open('recipes.txt', 'r', encoding='utf-8')
    cook_book = {}

    new_rec = True
    for line in cook_book_file:
        # print(line)
        if line.isspace():
            # new  recipe
            new_rec = True
            continue

        stripped_line = line.strip()
        list_line = stripped_line.split('|')

        if new_rec:
            dish = stripped_line
            cook_book[dish] = []
            new_rec = False
            continue

        if len(list_line) > 1:
            cook_book[dish].append(dict(ingredient_name=list_line[0], quantity=int(list_line[1]), measure=list_line[2]))

    cook_book_file.close()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):

    new_cook_book = read_recipes_from_file()
    ingredients_dict = {}
    for dish in dishes:
        if dish in new_cook_book:
            for ing in new_cook_book[dish]:
                if ing['ingredient_name'] in ingredients_dict:
                    ingredients_dict[ing['ingredient_name']]['quantity'] += ing['quantity']*person_count
                else:
                    ingredients_dict[ing['ingredient_name']] = dict(measure=ing['measure'], quantity=ing['quantity']*person_count)

    return ingredients_dict


print('Задача 1. Считываем рецепты из файла', '\n')
new_cook_book = read_recipes_from_file()
pprint(new_cook_book)
print()

print('Задача 2. Получаем ингредиенты', '\n')
print('Фахитос, Омлет (дублируются помидоры)')
ingredients = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(ingredients)
print()
print('Запеченный картофель, Омлет')
ingredients = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(ingredients)
print()