from find_highest_number import HighestNumberFinder


def test_find_highest_in_empty_array():
    # arrange
    numbers = [33]
    expectedResult = 33
    cut = HighestNumberFinder()

    # act 
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result


def test_find_highest_in_array_of_two_descending():
    # arrange
    numbers = [14, 7]
    expectedResult = 14
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result


def test_find_highest_in_array_of_Random():
    # arrange
    numbers = [64, 22, 82, 46, 64, 82, 64, 64, 3, 9, 1, 19, 20]
    expectedResult = 82
    cut = HighestNumberFinder()

    # act
    result = cut.find_highest_number(numbers)
    # assert

    assert expectedResult == result
