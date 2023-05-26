from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


def helper_view(request, recipe=None, servings=1):

    if recipe == None:
        return HttpResponse ('Рецепт не введён!')

    else:
        mult = int(servings)

        if mult == 1:
            context = {'recipe': DATA[recipe]}
        else:
            dict_mult = {}
            for k, v in DATA[recipe].items():
                v1 = v * mult
                dict_mult[k] = v1
            context = {'recipe': dict_mult}

        return render(request, 'calculator/index.html', context)

    # return render(request, 'index.html', context)
    # return HttpResponse ('DATA')

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
