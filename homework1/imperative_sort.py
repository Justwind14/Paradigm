def imperative_bubble_sort(arr):
    """
    метод сортировки пузырьком в императивной парадигме

    :param arr: Массив для сортирвоки 
    :type arr: list
    :return: Nothing
    """
    # заводим переменную 'n' под длину массива
    n = len(arr)

    for i in range(n-1):
        for j in range(1, n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                
    print(arr)


