def is_multiple(n: int, m: int) -> bool:
    """Check if n is an integer multiple of m.
    >>> is_multiple(10, 5)
    True
    >>> is_multiple(10, 0)
    False
    >>> is_multiple(0, 0)
    True
    """
    if m == 0:
        return False
    return n % m == 0

if __name__ == "__main__":
    from doctest import testmod
    testmod()