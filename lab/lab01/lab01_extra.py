"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    product = 1
    while k>0:
        k = k - 1
        product = product * n
        n = n - 1
    return product
print(falling(6,3))
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    first_eight = 0
    second_eight = 0
    while n/10 > 0:
        first_eight = n % 10
        if first_eight == 8:
            second_eight = n // 10 % 10
            if  second_eight == 8:
                return True
        n = n // 10
    return False
print(double_eights(8))