def mod_exp(base: int, exponent: int, modulus: int):
    """Fast modular exponentiation algorithm.
       Computes c when c and b^e are congruent modulo n
    Args:
        base (int): base of of RHS
        exponent (int): exponent of RHS
        modulus (int): modulus of congruence

    Returns:
        _type_: _description_
    """
    if modulus == 1:
        return 0
    c = 1
    for e_prime in range(0, exponent):
        c = (c * base) % modulus
    return c


if __name__ == "__main__":
    print(mod_exp(4, 13, 497))
