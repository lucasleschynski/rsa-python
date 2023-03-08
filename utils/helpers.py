def mod_exp(b: int, e: int, m: int) -> int:
    """Fast modular exponentiation algorithm.
       Computes r when r and b^e are congruent modulo n
    Args:
        base (int): base of of RHS
        exponent (int): exponent of RHS
        modulus (int): modulus of congruence

    Returns:
        int: result of modular exponentiation
    """
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1:
            r = (r * b) % m
    return r


def carmichael_totient(p: int, q: int) -> int:
    """Performs the carmichael totient function (lambda) on n, or p * q

    Returns:
        int: lambda(n)
    """

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return lcm(p - 1, q - 1)


def extended_euclidean(a: int, b: int) -> int:
    """Solves Bézout's identity {ax + by = gcd(a,b)}
    where a = e and b = lambda(n) = carmichael_totient(p, q).
    This is another form of d * e = 1 (mod lambda(n)), so solving for x gives p.

    Returns:
        int: Bézout x coefficient, used as the private key
    """
    prevx, x = 1, 0
    while b:
        q = a // b
        x, prevx = prevx - q * x, x
        a, b = b, a % b

    return prevx


if __name__ == "__main__":
    print(mod_exp(4, 13, 497))
