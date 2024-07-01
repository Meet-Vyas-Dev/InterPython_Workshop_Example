"""Tests for statistics functions within the Model layer."""

import pandas as pd

# def test_max_mag_integers():
#     # Test that max_mag function works for integers
#     from lcanalyzer.models import max_mag

#     test_input_df = pd.DataFrame(data=[[1, 5, 3], 
#                                        [7, 8, 9], 
#                                        [3, 4, 1]], columns=list("abc"))
#     test_input_colname = "a"
#     test_output = 7

#     assert max_mag(test_input_df, test_input_colname) == test_output

# def test_max_mag_zeros():
#     # Test that max_mag function works for zeros
#     from lcanalyzer.models import max_mag

#     test_input_df = pd.DataFrame(data=[[0, 0, 0], 
#                                        [0, 0, 0], 
#                                        [0, 0, 0]], columns=list("abc"))
#     test_input_colname = "b"
#     test_output = 0

#     assert max_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_negatives():
    # Test that min_mag function works for negatives
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[-7, -7, -3], [-4, -3, -1], [-1, -5, -3]], columns=list("abc"))
    test_input_colname = "b"
    test_output = -7

    assert min_mag(test_input_df, test_input_colname) == test_output



def test_mean_mag_integers():
    # Test that mean_mag function works for negatives
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[-7, -7, -3], [-4, -3, -1], [-1, -5, -3]], columns=list("abc"))
    test_input_colname = "a"
    test_output = -4.

    assert mean_mag(test_input_df, test_input_colname) == test_output

### Get maximum values for all bands
def calc_stat(lc, bands, mag_col):
    import lcanalyzer.models as models
    # Define an empty dictionary where we will store the results
    stat = {}
    # For each band get the maximum value and store it in the dictionary
    for b in bands:
        stat[b + "_max"] = models.max_mag(lc[b], mag_col)
    return stat

def test_calc_stat():
    # Mock light curve data as a dictionary of DataFrames
    lc = {
        'band1': pd.DataFrame({'mag': [10, 12, 14, 11]}),
        'band2': pd.DataFrame({'mag': [20, 19, 17, 18]}),
        'band3': pd.DataFrame({'mag': [30, 29, 28, 31]}),
    }

    # List of bands to test
    bands = ['band1', 'band2', 'band3']
    
    # Column name for magnitudes
    mag_col = 'mag'

    # Expected output
    expected_output = {
        'band1_max': 14,
        'band2_max': 20,
        'band3_max': 31,
    }

    # Calculate the actual output using the function
    actual_output = calc_stat(lc, bands, mag_col)
    
    # Assert that the actual output matches the expected output
    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

import pytest
def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)

@pytest.mark.parametrize(
    "test_df, test_colname, expected",
    [
        (pd.DataFrame(data=[[1, 5, 3], 
                            [7, 8, 9], 
                            [3, 4, 1]], 
                      columns=list("abc")),
        "a",
        7),
        (pd.DataFrame(data=[[0, 0, 0], 
                            [0, 0, 0], 
                            [0, 0, 0]], 
                      columns=list("abc")),
        "b",
        0),
    ])
def test_max_mag(test_df, test_colname, expected):
    """Test max function works for array of zeroes and positive integers."""
    from lcanalyzer.models import max_mag
    assert max_mag(test_df, test_colname) == expected