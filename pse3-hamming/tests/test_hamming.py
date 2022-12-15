import pytest

from hamming import hamming_distance
from hamming import hamming_distance1

def test_hamming_distance_returns_correct_diff():
    # ^rename with meaningful test name
    # and complete test implementation below
    # pass
    # arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"
    # act
    hamming_diff = hamming_distance1(strand1,strand2)
    # assert
    assert(hamming_diff == 7)
    
def test_empty_string():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    strand1 = ""
    strand2 = ""
    # act
    hamming_diff = hamming_distance1(strand1,strand2)
    # assert
    assert(hamming_diff == 0)