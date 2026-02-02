def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    This is more efficient than the recursive version.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fibonacci_sequence(count):
    """
    Generate a list of Fibonacci numbers.
    
    Args:
        count (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: A list containing the first 'count' Fibonacci numbers
    
    Raises:
        ValueError: If count is negative
    """
    if count < 0:
        raise ValueError("count must be a non-negative integer")
    
    if count == 0:
        return []
    
    if count == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    
    return sequence


if __name__ == "__main__":
    # Example usage
    print("Fibonacci calculation examples:")
    print("-" * 40)
    
    # Calculate specific Fibonacci numbers
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    
    print("\n" + "-" * 40)
    print("Using iterative approach:")
    print(f"fibonacci_iterative(15) = {fibonacci_iterative(15)}")
    
    print("\n" + "-" * 40)
    print("First 15 Fibonacci numbers:")
    print(fibonacci_sequence(15))
