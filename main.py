# вводим последовательность чисел
array = input("Введите число через пробел:")
# преобразуем строку с числами в список целых чисел
array_list = [int(i) for i in array.split()]

# вводим число, с которым будем сравнивать элементы списка
n_user = input("Введите число:")
# проверяем, что введено целое число
if n_user.isdigit():
    # преобразуем строку с числом в целое число
    n_user = int(n_user)

    # добавляем введенное число в список
    array_list.append(n_user)

    # сортируем список
    array_list = sorted(array_list)

    # ищем позицию, на которой должно находиться введенное число
    def bi_search(a: int, array: list) -> int:
        left, right = 0, len(array)
        while left < right:
            middle = (left + right) // 2
            if array[middle] < a:
                left = middle + 1
            else:
                right = middle
        return left

    number_index = bi_search(n_user, array_list)

    # проверяем, что позиция не выходит за пределы списка
    if number_index >= len(array_list):
        print("Число больше всех элементов списка")
    elif number_index == 0:
        print("Число меньше всех элементов списка")
    else:
        # находим индексы элементов, соседствующих с введенным числом
        left_index = number_index - 1
        right_index = number_index
        # выводим результаты
        print("Индекс введенного числа:", number_index)
        print("Список после сортировки:", array_list)
        print("Индекс соседних чисел:", left_index, right_index)
