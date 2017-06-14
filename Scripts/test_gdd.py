'''
    Unit test for calc_gdd function
'''
from calc_gdd import *
from numpy.testing import assert_allclose

def test_first_empty():
    ''' Tests edge case: the first list is empty '''
    observed = calc_gdd([],[1],10,30)
    expected = None
    assert observed == expected

def test_second_empty():
    ''' Tests edge case: the second list is empty '''
    observed = calc_gdd([1],[],10,30)
    expected = None
    assert observed == expected

def test_all_empty():
    ''' Tests corner case: the first list is empty '''
    observed = calc_gdd([],[],10,30)
    expected = ([], [])
    assert observed == expected

def test_first_longer():
    ''' Tests the case when the first list is longer than the second '''
    observed = calc_gdd([1, 2],[3],10,30)
    expected = None
    assert observed == expected

def test_second_longer():
    ''' Tests the case when the second list is longer than the first '''
    observed = calc_gdd([1],[2, 3],10,30)
    expected = None
    assert observed == expected

def test_tbase_greater_tupper():
    ''' Tests if Tbase is greater than Tupper '''
    observed = calc_gdd([1],[1],30,10)
    expected = None
    assert observed == expected

def test_plain_data():
    ''' Tests plain data calculation '''
    observed = calc_gdd([11, 12, 13],[24, 25, 26],10,30)
    expected = ([7.5, 8.5, 9.5], [7.5, 16. , 25.5])
    assert_allclose(observed, expected, rtol=1e-6)

def test_min_less_than_tbase():
    ''' Tests edge case: the first list data is smaller than Tbase '''
    observed = calc_gdd([1, 2, 3],[24, 25, 26],10,30)
    expected = ([7, 7.5, 8], [7, 14.5, 22.5])
    assert_allclose(observed, expected, rtol=1e-6)

def test_max_greater_than_tupper():
    ''' Tests edge case: the second list data is greater than Tupper '''
    observed = calc_gdd([11, 12, 13],[34, 35, 36],10,30)
    expected = ([10.5, 11, 11.5], [10.5, 21.5, 33.0])
    assert_allclose(observed, expected, rtol=1e-6)

def test_both_less_than_tbase():
    ''' Tests corner case: the both list data is smaller than Tbase '''
    observed = calc_gdd([1, 2, 3],[4, 5, 6],10,30)
    expected = ([0. , 0. , 0. ], [0. , 0. , 0.])
    assert_allclose(observed, expected, rtol=1e-6)

def test_both_greater_than_tupper():
    ''' Tests corner case: the both list data is greater than Tupper '''
    observed = calc_gdd([31, 32, 33],[34, 35, 36],10,30)
    expected = ([20. , 20. , 20. ], [20.0, 40.0, 60.0])
    assert_allclose(observed, expected, rtol=1e-6)

def test_min_less_than_tbase_max_greater_than_tupper():
    '''
        Tests corner case: the first list data is smaller than Tbase
        and the second list data is greater than Tupper
    '''
    observed = calc_gdd([1, 2, 3],[34, 35, 36],10,30)
    expected = ([10. , 10. , 10. ], [10.0, 20.0, 30.0])
    assert_allclose(observed, expected, rtol=1e-6)

def test_tmin_greater_tmax():
    ''' Tests if Tmin is greater than Tmax '''
    observed = calc_gdd([1, 32, 3],[4, 5, 6],10,30)
    expected = None
    assert observed == expected

def test_tmin_not_a_number():
    ''' Tests if some of Tmin is not a number '''
    observed = calc_gdd([1, 'a', 3],[4, 5, 6],10,30)
    expected = None
    assert observed == expected

def test_tmax_not_a_number():
    ''' Tests if some of Tmax is not a number '''
    observed = calc_gdd([1, 2, 3],[4, 5, 'a'],10,30)
    expected = None
    assert observed == expected

def test_tmin_tmax_not_a_number():
    ''' Tests if both Tmin and Tmax at the same position are not numbers '''
    observed = calc_gdd([1, 'a', 3],[4, 'b', 6],10,30)
    expected = None
    assert observed == expected


def test_tbase_not_a_number():
    ''' Tests if tbase not a number '''
    observed = calc_gdd([1, 2, 3],[4, 5, 6], 'a', 30)
    expected = None
    assert observed == expected

def test_tupper_not_a_number():
    ''' Tests if tupper is not a number '''
    observed = calc_gdd([1, 2, 3],[4, 5, 6], 10, 'b')
    expected = None
    assert observed == expected

def test_tbase_tupper_not_a_number():
    ''' Tests if both tbase and tupper are not numbers '''
    observed = calc_gdd([1, 2, 3],[4, 5, 6], 'a', 'b')
    expected = None
    assert observed == expected
