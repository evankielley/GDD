from calc_gdd import *
from numpy.testing import assert_allclose

def test_all_empty():
    observed = calc_gdd([],[],10,30)
    expected = ([], [])
    assert observed == expected

def test_first_empty():
    observed = calc_gdd([],[1],10,30)
    expected = None
    assert observed == expected

def test_second_empty():
    observed = calc_gdd([1],[],10,30)
    expected = None
    assert observed == expected

def test_first_longer():
    observed = calc_gdd([1, 2],[3],10,30)
    expected = None
    assert observed == expected

def test_second_longer():
    observed = calc_gdd([1],[2, 3],10,30)
    expected = None
    assert observed == expected

def test_tbase_greater_tupper():
    observed = calc_gdd([1],[1],30,10)
    expected = None
    assert observed == expected

def test_plain_data():
    observed = calc_gdd([11, 12, 13],[24, 25, 26],10,30)
    expected = ([7.5, 8.5, 9.5], [7.5, 16. , 25.5])
    assert_allclose(observed, expected, rtol=1e-6)

def test_min_less_than_tbase():
    observed = calc_gdd([1, 2, 3],[24, 25, 26],10,30)
    expected = ([7, 7.5, 8], [7, 14.5, 22.5])
    assert_allclose(observed, expected, rtol=1e-6)

def test_max_greater_than_tupper():
    observed = calc_gdd([11, 12, 13],[34, 35, 36],10,30)
    expected = ([10.5, 11, 11.5], [10.5, 21.5, 33.0])
    assert_allclose(observed, expected, rtol=1e-6)

def test_both_less_than_tbase():
    observed = calc_gdd([1, 2, 3],[4, 5, 6],10,30)
    expected = ([0. , 0. , 0. ], [0. , 0. , 0.])
    assert_allclose(observed, expected, rtol=1e-6)

def test_both_greater_than_tupper():
    observed = calc_gdd([31, 32, 33],[34, 35, 36],10,30)
    expected = ([20. , 20. , 20. ], [20.0, 40.0, 60.0])
    assert_allclose(observed, expected, rtol=1e-6)

def test_min_less_than_tbase_max_greater_than_tupper():
    observed = calc_gdd([1, 2, 3],[34, 35, 36],10,30)
    expected = ([10. , 10. , 10. ], [10.0, 20.0, 30.0])
    assert_allclose(observed, expected, rtol=1e-6)

def test_tmin_greater_tmax():
    observed = calc_gdd([1, 32, 3],[4, 5, 6],10,30)
    expected = None
    assert observed == expected

def test_tmin_not_a_number():
    observed = calc_gdd([1, 'a', 3],[4, 5, 6],10,30)
    expected = None
    assert observed == expected

def test_tmax_not_a_number():
    observed = calc_gdd([1, 2, 3],[4, 5, 'a'],10,30)
    expected = None
    assert observed == expected
