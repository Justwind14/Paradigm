# Контекст
# Предположим, что мы хотим найти элемент в массиве (получить
# его индекс). Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно
# использовать бинарный поиск. Принцип прост: сначала берём
# элемент находящийся посередине и сравниваем с тем, который мы
# хотим найти. Если центральный элемент больше нашего,
# рассматриваем массив слева от центрального, а если больше -
# справа и повторяем так до тех пор, пока не найдем наш элемент.

# ● Ваша задача
# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


def binary_search(someList: list) -> function:
    """Функция поиска числа в массиве чисел.

    :params:
        - someList: массив чисел

    :type someList: list

    :return: Возвращает результат внутренней функции binary_search_helper
    """

    def binary_search_helper(someList: list, number: int) -> int:
        """Внутренняя функция, хранящая в себе алгоритм бинарного поиска.

        :params:
            - someList: массив чисел
            - искомое число

        :type someList: list
        :tyoe number: int

        :return: Возвращает искомое число, если он присутствует в масиве, либо -1, если такого числа в принимаемом массиве нет
        """

        # создаем переменную, хранящую в себе индекс среднего элемента массива
        delimiter = len(someList) // 2

        if someList[delimiter] > number:
            return binary_search_helper(someList[:delimiter], number)
        if someList[delimiter] < number:
            return binary_search_helper(someList[delimiter:], number)
        if someList[delimiter] == number:
            return someList[delimiter]
        else:
            return -1

    if len(someList) != 0:
        # возвращаем результат работы внутренней функции с искомым параметром number
        return lambda number: binary_search_helper(someList, number)
    else:
        # если массив пустой, вызов функции ничего не вернет
        return None

# входные данные: массив и искомое в массиве число
anyList = [1, 3, 6, 11, 22, 55, 71, 79]
required_number = 79

# вызов функциии бинарног опоиска
binary = binary_search(anyList)
if binary is not None:
    result = binary(required_number)
    if result == -1:
        print("искомый элемент не найден")
    else:
        print(
            f"число {required_number} находится на {anyList.index(result)}й позиции в списке {anyList}"
        )
else:
    print("зачем вы проверяете пустой массив?")
