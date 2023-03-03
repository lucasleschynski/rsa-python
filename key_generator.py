from utils.prime_generator import PrimeGenerator
from key import Key


class KeyGenerator:
    def __init__(self) -> None:
        self.pg = PrimeGenerator()
        self.e = 2**16 + 1

    def generate_primes(self, nbits: int) -> tuple[int, int, int]:
        """Generates primes p, q, n
        p and q both have (nbits) bits

        Returns:
            tuple[int, int, int]: p, q, and n
        """

        def check_valid_bitlength(nbits: int):
            if (nbits & (nbits - 1) == 0) and nbits != 0:
                return True
            return False

        if not check_valid_bitlength(nbits):
            raise ValueError("Bit length must be a power of two")

        primebits = (int)(nbits / 2)

        # TODO: Ensure that n is exactly n bits, (i.e. if p/q are 64 bits n is 128 not 127)
        p, q, n = 0, 0, 0
        while n.bit_length() != nbits:
            p = self.pg.generate_prime(primebits)
            q = self.pg.generate_prime(primebits)
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
            q = a // b
            x, prevx = prevx - q * x, x
            a, b = b, a % b

        return prevx

    def generate_public_key(self, nbits) -> tuple[int, int, int]:
        """Public key generator

        Returns:
            tuple[int, int, int]: n, e, and lambda(n) (or totient)
        """
        p, q, n = self.generate_primes(nbits)
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
            # d, totient)
        return d

    def generate_key(self, nbits) -> Key:
        """Generates whole keypair (public and private)

        Returns:
            tuple[tuple[int, int], int]: (n, e), d
        """
        n, e, totient = self.generate_public_key(nbits)
        d = self.generate_private_key(totient)
        print(f"\n\nGenerated n: {n}\n\nGenerated e: {e}\n\nGenerated d: {d}")
        return Key((n, e), d, nbits)
