import math

# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


def pirson_correlation(list1, list2):
    """
    функция расчета корреляции Пирсона между двумя массивами.

    :params:
     - list1: первый массив значений
     - list2: второй массив значений

    :type list1, list2: list

    :return: Возвращает корреляцию Пирсона между списками чисел list1 и list2
    """

    # Проверка необходимости одинаковой длины поступающих в функцию списков
    if len(list1) != len(list2):
        raise ValueError("Массивы должны быть одинаковой длины")

    list_length = len(list2)

    # высчитываем средние значения по x и по y
    M_x = sum(list1) / list_length
    M_y = sum(list2) / list_length

    denumerator_x = sum([(xi - M_x) ** 2 for xi in list1]) / len(list1)
    denumerator_y = sum([(yi - M_y) ** 2 for yi in list2]) / len(list2)
    numerator = sum([(xi - M_x) * (yi - M_y) for xi, yi in zip(list1, list2)]) / len(
        list1
    )
    return numerator / (math.sqrt(denumerator_x * denumerator_y))


# Входные данные:
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [16, 17, 18, 19, 15, 16, 12, 22]

# Вывод результата(корреляции). Корреляция может принимать значения от -1 до 1,
# где -1 означает полную отрицательную корреляцию, 0 - отсутствие корреляции,
# а 1 - полную положительную корреляцию.
print(f"Корреляция Пирсона составляет: {pirson_correlation(list1, list2)}")
