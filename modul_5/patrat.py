def patrat(x):
    """Returneaza patratul lui x.
    >>> patrat(2)
    4
    >>> patrat(-2)
    4
    """
    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
