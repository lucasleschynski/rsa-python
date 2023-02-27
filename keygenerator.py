from primegenerator import PrimeGenerator


class KeyGenerator:
    def __init__(self):
        self.p, self.q = None, None
        self.n = self.generate_n(64)
        # print(type(self.generate_n(256)))
        print(self.carmichael_totient(self.p, self.q))

    def generate_n(self, nbits):
        pg = PrimeGenerator()
        self.p = pg.generate_prime(nbits)
        self.q = pg.generate_prime(nbits)
        self.n = self.p * self.q
        print(
            f"Generated p: {self.p}\n\nGenerated q: {self.q}\n\nGenerated n: {self.n}\n    N's bit length: {self.n.bit_length()}"
        )
        return self.n

    def carmichael_totient(self, p, q):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) / gcd(p, q)

        return lcm(p - 1, q - 1)
