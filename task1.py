from typing import Union, List


CustomList = List[Union[int, str]]

# Сложность O(log n)
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


print(task('111111111111111111111111100000000'))
print(task(['1', 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]))


if __name__ == "__main__": 
    import doctest
    doctest.testmod()
