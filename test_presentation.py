from presentation import elem, elem2, factorial, factorial2, _map, _map2


# elem
assert elem(1, [1,2]) == True
assert elem(3, [1,2]) == False
assert elem(4, [1,2]) == False
assert elem(4, [4]) == True
assert elem(1, []) == False

# elem2
assert elem2(1, [1,2]) == True
assert elem2(4, [4]) == True
assert elem2(3, [1,2]) == False
assert elem2(4, [1,2]) == False
assert elem2(1, []) == False

# factorial
def test_factorial_of_1_is_1():
    assert factorial(1) == 1

def test_factorial_of_2_is_2():
    assert factorial(2) == 2

def test_factorial_of_3_is_6():
    assert factorial(3) == 6

def test_factorial_of_4_is_24():
    assert factorial(4) == 24

# factorial2
def test_factorial2_of_1_is_1():
    assert factorial2(1) == 1

def test_factorial2_of_2_is_2():
    assert factorial2(2) == 2

def test_factorial2_of_3_is_6():
    assert factorial2(3) == 6

def test_factorial2_of_4_is_24():
    assert factorial2(4) == 24

# _map
def test_map_plus_1_in_empty_list():
    assert _map(lambda x: x + 1, []) == []

def test_map_plus_1_in_list_just_with_1():
    assert _map(lambda x: x + 1, [1]) == [2]

def test_map_plus_1_in_a_list_with_3():
    assert _map(lambda x: x + 1, [1,2,3,4]) == [2,3,4,5]

# _map2
def test_map2_plus_1_in_empty_list():
    assert _map2(lambda x: x + 1, []) == []

def test_map2_plus_1_in_list_just_with_1():
    assert _map2(lambda x: x + 1, [1]) == [2]

def test_map2_plus_1_in_a_list_with_3():
    assert _map2(lambda x: x + 1, [1,2,3,4]) == [2,3,4,5]
