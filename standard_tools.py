import math

def calculate_standard_deviation(data, mean = None):
    """Calculate the standard deviation of a list of numbers."""
    n = len(data)
    if n == 0:
        return 0
    
    if mean is None:
        mean = sum(data) / n

    variance = sum((x - mean) ** 2 for x in data) / n
    return math.sqrt(variance)

def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    n = len(data)
    if n == 0:
        return 0
    return sum(data) / n