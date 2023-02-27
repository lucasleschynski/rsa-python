import primegenerator as pg

bits = 8
pg.generate_prime(bits)

p = pg.generate_prime(bits)
q = pg.generate_prime(bits)

n = p * q


def carmichael_totient(p, q):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) / gcd(p, q)

    return lcm(p - 1, q - 1)
