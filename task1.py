from typing import Union, List


CustomList = List[Union[int, str]]

# Сложность алгоритма O(log n)
# В тексте задания было сказано, что за последовательностью единиц следуют нули, 
# поэтому вариант с отсутствием нуля не учитывал
def task(array: Union[CustomList, str]):
    """Возвращает первое вхождение 0 в массив
    >>> task('111111111111111111111111100000000')
    'OUT:25'

    >>> task(['1', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
    'OUT:7'

    >>> task(['1', '1', '1', '1', '1', '0'])
    'OUT:5'
    """

    left = 0
    right = len(array) - 1
    item = 0
    while right - left > 1:
        middle = (left + right) // 2
        if int(array[middle]) == 0:
            right = middle
        elif int(array[middle]) > 0:
            left = middle
    return f'OUT:{right}'


if __name__ == "__main__": 
    import doctest
    doctest.testmod()
    print(task('111111111111111111111111100000000'))
    print(task(['1', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]))
