"""This script deals with prime numbers."""
def is_prime(n):
    """Returns True if a number is prime, False otherwise."""
    # Create a loop
    for i in range(2, n):
        # Check if n is divisble by i.
        if n % i == 0:
            return False
            break # Break out of the program.
        else:
            return True


def find_primes(x):
    """Returns a list of prime numbers up to a given number."""
    primes = []
    for i in range(x+1):
        if is_prime(i):
            primes.append(i)
    return primes
