def is_factor(a, b):
    """
    Returns True if a is a factor of b, false otherwise.

    # Examples:
     * `is_factor(7, 21)` would evaluate to `True`. 
     * `is_factor(4, 9)` would evaluate to `False`. 
    """
    if b % a == 0:
        return True
    else:
        return False


def find_factors(n):
    """
    Returns the factors of a given number in a list.
    # Examples:
    * `find_factors(24)` would give `[1, 2, 3, 4, 6, 8, 12, 24]`.
    * `find_factors(12)` would give `[1, 2, 3, 4, 6, 12]`.
    * `find_factors(7)` would give `[1, 7]`.
    """
    factors = []
    for i in range(1, n+1):
        if is_factor(i, n):
            factors.append(i)
    return factors
