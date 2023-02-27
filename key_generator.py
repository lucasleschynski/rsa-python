from prime_generator import PrimeGenerator


class KeyGenerator:
    def __init__(self, nbits: int) -> None:
        self.pg = PrimeGenerator()
        self.nbits = nbits
        self.e = 2**16 + 1

        pubkey, privkey = self.generate_key()

    def generate_primes(self, nbits: int) -> tuple[int, int, int]:
        """Generates primes p, q, n
        p and q both have (nbits) bits

        Returns:
            tuple[int, int, int]: p, q, and n
        """
        p = self.pg.generate_prime(nbits)
        q = self.pg.generate_prime(nbits)
        n = p * q
        print(
            f"Generated p: {p}\n\nGenerated q: {q}\n\nGenerated n: {n}\n    N's bit length: {n.bit_length()}"
        )
        return p, q, n

    def carmichael_totient(self, p: int, q: int) -> int:
        """Performs the carmichael totient function (lambda) on n, or p * q

        Returns:
            int: lambda(n)
        """

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return abs(a * b) / gcd(p, q)

        return lcm(p - 1, q - 1)

    def extended_euclidean(self, a: int, b: int) -> int:
        """Solves Bézout's identity {ax + by = gcd(a,b)}
        where a = e and b = lambda(n) = carmichael_totient(p, q).
        This is another form of d * e = 1 (mod lambda(n)), so solving for x gives p.

        Returns:
            int: Bézout x coefficient, used as the private key
        """
        prevx, x = 1, 0
        while b:
            q = a / b
            x, prevx = prevx - q * x, x
            a, b = b, a % b

        return prevx

    def generate_public_key(self) -> tuple[int, int, int]:
        """Public key generator

        Returns:
            tuple[int, int, int]: n, e, and lambda(n) (or totient)
        """
        p, q, n = self.generate_primes(self.nbits)
        totient = self.carmichael_totient(p, q)
        return n, self.e, totient

    def generate_private_key(self, totient: int) -> int:
        """Private key generator
        Gets d value, then adds totient until d > 0.
        d * e = 1 (mod lambda(n) still holdswhen adding a multiple of the totient.

        Returns:
            int: _description_
        """
        d = self.extended_euclidean(self.e, totient)
        while d < 0:
            d += totient
            print(d, totient)
        return d

    def generate_key(self) -> tuple[tuple[int, int], int]:
        """Generates whole keypair (public and private)

        Returns:
            tuple[tuple[int, int], int]: (n, e), d
        """
        n, e, totient = self.generate_public_key()
        d = self.generate_private_key(totient)
        print(f"\n\nGenerated n: {n}\n\nGenerated e: {e}\n\nGenerated d: {d}")
        return (n, e), d
