import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    arr = np.asarray(x, dtype = 'float')
    result = []
    for num in np.atleast_1d(arr):
        Value = 1/(1 + (np.exp(-num)))  #np.exp(x) use numPy array,& math.exp(x) use individual
        result.append(Value)

    if arr.ndim == 0:  # check the dimention  
        return result[0]
        
    return np.array(result)   # return the whole array 
    
    