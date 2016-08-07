def elem(element, _list):
    return element in _list

def elem2(element, _list):
    if _list == []:
        return False

    if element == _list[0]:
        return True
    else:
        return elem2(element, _list[1:])

def factorial(number):
    result = 1

    for index in range(1, number+1):
        result = result * index

    return result

def factorial2(number):
    if number == 1: return 1

    return number * factorial2(number-1)


def _map(func, _list):
    return [func(x) for x in _list]

def _map2(func, _list):
    if _list == []: return []

    return [func(_list[0])] + _map2(func, _list[1:])

def quicksort(_list):
    if _list == []:
        return []

    pivot = _list[0]

    smallers = [x for x in _list if x < pivot]
    biggers = [x for x in _list if x > pivot]

    return smallers + [pivot] + biggers
