from primegenerator import PrimeGenerator


class KeyGenerator:
    def __init__(self, nbits):
        self.pg = PrimeGenerator()
        self.nbits = nbits
        self.e = 2**16 + 1

        pubkey, privkey = self.generate_key()

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

    def generate_public_key(self):
        p, q, n = self.generate_primes(self.nbits)
        totient = self.carmichael_totient(p, q)
        return n, self.e, totient

    def generate_private_key(self, totient):
        p = self.extended_euclidean(self.e, totient)
        while p < 0:
            p += totient
            print(p, totient)
        return p

    def generate_key(self):
        n, e, totient = self.generate_public_key()
        d = self.generate_private_key(totient)
        print(f"\n\nGenerated n: {n}\n\nGenerated e: {e}\n\nGenerated d: {d}")
        return (n, e), d
