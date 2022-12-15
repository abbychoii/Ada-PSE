import pytest

from pairs_with_given_sum_pse_review import pairs_with_given_sum

def test_valid_input():
    numbers = [1,2,4,5]
    target = 6
    assert pairs_with_given_sum(numbers, target) == 2
def test_non_ordered_input():
    numbers =[97, 51, 49, 35, 3, 65]
    target = 100
    assert pairs_with_given_sum(numbers, target) == 3