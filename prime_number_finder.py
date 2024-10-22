def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate a list of prime numbers up to the specified limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input: Limit for prime numbers
limit = int(input("Enter the limit up to which you want to find prime numbers: "))
prime_numbers = generate_primes(limit)

print(f"Prime numbers up to {limit}: {prime_numbers}")
