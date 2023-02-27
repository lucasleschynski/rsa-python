from primegenerator import PrimeGenerator
from primegenerator import PrimeGenerator


class KeyGenerator:
    def __init__(self):
        self.pg = PrimeGenerator()
        # self.p, self.q = None, None
        # self.n = self.generate_n(64)
        self.e = 2**16 + 1  # 65537
        self.totient = self.carmichael_totient(self.p, self.q)
        self.d = self.extended_euclidean(self.e, self.totient)

    def generate_primes(self, nbits):
        p = self.pg.generate_prime(nbits)
        q = self.pg.generate_prime(nbits)
        n = p * q
        print(
            f"Generated p: {p}\n\nGenerated q: {q}\n\nGenerated n: {n}\n    N's bit length: {n.bit_length()}"
        )
        return p, q, n

    def carmichael_totient(self, p, q):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return abs(a * b) / gcd(p, q)

        return lcm(p - 1, q - 1)

    def extended_euclidean(self, a, b):
        prevx, x = 1, 0
        while b:
            q = a / b
            x, prevx = prevx - q * x, x
            a, b = b, a % b

        return prevx

    def generate_public_key(self, nbits):
        p, q, n = self.generate_primes(nbits)
        e = 2**16 + 1
        totient = self.carmichael_totient(p, q)
        return n, e

    def generate_private_key(self, e, totient):
        p = self.extended_euclidean(e, totient)
        return p
