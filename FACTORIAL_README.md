# Factorial Function

A simple Python function that calculates the factorial of a non-negative integer with proper error handling and comprehensive documentation.

## Overview

The `factorial()` function computes the factorial of a non-negative integer n, denoted as n!. The factorial is the product of all positive integers less than or equal to n. By mathematical definition, 0! = 1.

## Features

- ✅ **Proper Error Handling**: Validates input types and values
- ✅ **Comprehensive Docstrings**: Detailed documentation following Python best practices
- ✅ **Iterative Implementation**: Avoids recursion depth limitations
- ✅ **Type Safety**: Raises appropriate exceptions for invalid inputs
- ✅ **Well Tested**: Includes 7 comprehensive unit tests

## Installation

No installation required. Simply copy the `factorial.py` file to your project directory.

## Usage

### Basic Usage

```python
from factorial import factorial

# Calculate factorial of a number
result = factorial(5)
print(result)  # Output: 120
```

### Examples

```python
from factorial import factorial

# Base cases
print(factorial(0))   # Output: 1
print(factorial(1))   # Output: 1

# Small numbers
print(factorial(5))   # Output: 120
print(factorial(10))  # Output: 3628800

# Larger numbers
print(factorial(20))  # Output: 2432902008176640000
```

### Error Handling

```python
from factorial import factorial

# Handling negative numbers
try:
    factorial(-5)
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Factorial is not defined for negative integers, got -5

# Handling non-integer types
try:
    factorial(3.14)
except TypeError as e:
    print(f"Error: {e}")
    # Output: Error: Expected an integer, got float

try:
    factorial("5")
except TypeError as e:
    print(f"Error: {e}")
    # Output: Error: Expected an integer, got str
```

## Function Signature

```python
def factorial(n: int) -> int
```

### Parameters

- **n** (int): A non-negative integer for which to calculate the factorial

### Returns

- **int**: The factorial of n

### Raises

- **TypeError**: If n is not an integer
- **ValueError**: If n is negative

## Running Examples

Run the provided example script to see the function in action:

```bash
python3 factorial_example.py
```

## Running Tests

Run the comprehensive unit tests:

```bash
python3 -m unittest test_factorial.py -v
```

## Test Coverage

The test suite includes:
- ✅ Base cases (0! and 1!)
- ✅ Small positive integers (2-5)
- ✅ Larger positive integers (10, 15)
- ✅ Error handling for negative numbers
- ✅ Error handling for non-integer types (float, string, list, None)
- ✅ Edge case with boolean values

## Mathematical Background

The factorial function is defined as:

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

Special cases:
- 0! = 1 (by definition)
- 1! = 1

## Performance

The function uses an iterative approach rather than recursion, which:
- Avoids stack overflow for large values of n
- Provides O(n) time complexity
- Provides O(1) space complexity

## License

This code is provided as part of the ghcp-cli-in-actions-demo repository.
