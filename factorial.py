"""
Factorial calculation module.

This module provides a function to calculate the factorial of a non-negative integer
with proper error handling and input validation.
"""


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    The factorial of a non-negative integer n, denoted by n!, is the product of all
    positive integers less than or equal to n. By definition, 0! = 1.
    
    Args:
        n (int): A non-negative integer for which to calculate the factorial.
    
    Returns:
        int: The factorial of n.
    
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    
    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")
    
    # Value validation
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative integers, got {n}")
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial iteratively to avoid recursion depth issues
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result
