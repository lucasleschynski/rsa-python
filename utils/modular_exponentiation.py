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


if __name__ == "__main__":
    print(mod_exp(4, 13, 497))
