from array01 import main
import numpy as np

def test_main():
    """
    Test the main function.
    """
    # Create a list of numeric values.
    values = [12.23, 13.32, 100, 36.32]
    output = main(values)
    expected = np.array(values)
    
    assert np.array_equal(output, expected), "Wrong answer!"

def test_main_1():
    """
    Test the main function.
    """
    # Create a list of numeric values.
    values = [1, 4, True, "Hello"]
    output = main(values)
    expected = np.array(values)
    
    assert np.array_equal(output, expected), "Wrong answer!"