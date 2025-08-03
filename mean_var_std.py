import numpy as np

def calculate(numbers):
   
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    
    matrix = np.array(numbers).reshape(3, 3)
    
   
    mean = [
        matrix.mean(axis=0).tolist(),  # mean of each column
        matrix.mean(axis=1).tolist(),  # mean of each row
        matrix.mean().tolist()         # mean of the flattened matrix
    ]
    
    variance = [
        matrix.var(axis=0).tolist(),   # variance of each column
        matrix.var(axis=1).tolist(),   # variance of each row
        matrix.var().tolist()          # variance of the flattened matrix
    ]
    
    std_dev = [
        matrix.std(axis=0).tolist(),   # std dev of each column
        matrix.std(axis=1).tolist(),   # std dev of each row
        matrix.std().tolist()          # std dev of the flattened matrix
    ]
    
    max_vals = [
        matrix.max(axis=0).tolist(),   # max of each column
        matrix.max(axis=1).tolist(),   # max of each row
        matrix.max().tolist()          # max of the flattened matrix
    ]
    
    min_vals = [
        matrix.min(axis=0).tolist(),   # min of each column
        matrix.min(axis=1).tolist(),   # min of each row
        matrix.min().tolist()          # min of the flattened matrix
    ]
    
    sum_vals = [
        matrix.sum(axis=0).tolist(),   # sum of each column
        matrix.sum(axis=1).tolist(),   # sum of each row
        matrix.sum().tolist()          # sum of the flattened matrix
    ]
    
    
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_vals,
        'min': min_vals,
        'sum': sum_vals
    }
from mean_var_std import calculate


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(numbers)
print(result)  # This should display output in the terminal

