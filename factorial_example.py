#!/usr/bin/env python3
"""
Example usage of the factorial function.

This script demonstrates how to use the factorial function with various inputs
and proper error handling.
"""

from factorial import factorial


def main():
    """Demonstrate the factorial function usage."""
    print("Factorial Function Examples")
    print("=" * 50)
    
    # Example 1: Calculate factorial of small numbers
    print("\n1. Small positive integers:")
    for n in [0, 1, 2, 3, 4, 5]:
        result = factorial(n)
        print(f"   {n}! = {result}")
    
    # Example 2: Calculate factorial of larger numbers
    print("\n2. Larger positive integers:")
    for n in [10, 15, 20]:
        result = factorial(n)
        print(f"   {n}! = {result}")
    
    # Example 3: Error handling - negative numbers
    print("\n3. Error handling for negative numbers:")
    try:
        result = factorial(-5)
        print(f"   (-5)! = {result}")
    except ValueError as e:
        print(f"   Error: {e}")
    
    # Example 4: Error handling - non-integer types
    print("\n4. Error handling for non-integer types:")
    test_values = [3.14, "5", [5], None]
    for value in test_values:
        try:
            result = factorial(value)
            print(f"   factorial({value}) = {result}")
        except TypeError as e:
            print(f"   factorial({repr(value)}): Error - {e}")
    
    print("\n" + "=" * 50)
    print("Examples completed successfully!")


if __name__ == "__main__":
    main()
