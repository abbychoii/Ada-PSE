import pytest
from merging_sorted_lists_pse_review import *

def test_validate_list_correctly_returns_sorted_int_list():
    list1 = [1,2,4,5]
    list2 = [6]

    assert validate_list(list1) == list1
    assert validate_list(list2) == list2

def test_validate_list_raises_valueerror_with_non_int():
    with pytest.raises(ValueError):
        validate_list([1,2.43, 3, 4])

def test_validate_list_raises_valuerror_when_not_sorted():
    with pytest.raises(ValueError):
        validate_list([1,3,5,4])

def tests_merging_sorted_lists_positive():
    list1 = [1,2,4,5]
    list2 = [6]
    
    result = merge_sorted_lists(list1, list2)

    assert result == [1,2,4,5,6]

def tests_merging_sorted_lists_negative():
    list1 = [-30,-10,0, 15,16]
    list2 = [-20,-5,5]
    
    result = merge_sorted_lists(list1, list2)

    assert result == [-30, -20, -10, -5, 0, 5, 15, 16]