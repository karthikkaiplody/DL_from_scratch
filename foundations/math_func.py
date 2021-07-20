import numpy as np
from numpy import ndarray

# Function to square an n-dimensional array
def square(x: ndarray) -> ndarray:
    '''
    Square each element in the input ndarray
    '''
    return np.power(x, 2)

def leaky_relu(x: ndarray) -> ndarray:
    '''
    Apply "Leaky Relu" funtion to each element in ndarray
    '''
    return np.maximum(0.2 * x, x)

    
