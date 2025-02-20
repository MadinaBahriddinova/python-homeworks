def is_prime(n: int) -> bool:
    """Returns True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a positive integer: "))
print(f"{num} is prime: {is_prime(num)}")
