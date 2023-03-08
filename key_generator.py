from utils.prime_generator import PrimeGenerator
from utils.helpers import mod_exp, carmichael_totient, extended_euclidean
from key import Key, PublicKey, PrivateKey


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
        while n.bit_length() != nbits and p == q:
            p = self.pg.generate_prime(primebits)
            q = self.pg.generate_prime(primebits)
            n = p * q
        print(
            f"Generated p: {p}\n\nGenerated q: {q}\n\nGenerated n: {n}\n    N's bit length: {n.bit_length()}"
        )
        return int(p), int(q), int(n)

    def generate_public_key(self, nbits) -> tuple[PublicKey, int]:
        """Public key generator

        Returns:
            tuple[int, int, int]: n, e, and lambda(n) (or totient)
        """
        p, q, n = self.generate_primes(nbits)
        totient = carmichael_totient(
            p, q
        )  # TODO: Remove the need for returning totient with public key
        return (n, self.e), totient

    def generate_private_key(self, totient: int) -> PrivateKey:
        """Private key generator
        Gets d value, then adds totient until d > 0.
        d * e = 1 (mod lambda(n) still holdswhen adding a multiple of the totient.

        Returns:
            int: _description_
        """
        d = extended_euclidean(self.e, totient)
        while d < 0:
            d += totient
        return int(d)

    def generate_key(self, nbits) -> Key:
        """Generates whole keypair (public and private)

        Returns:
            tuple[tuple[int, int], int]: (n, e), d
        """
        # TODO: Clean up the variables names and references here
        public_key, totient = self.generate_public_key(nbits)
        print(f"Totient: {totient}")
        private_key = self.generate_private_key(totient)
        print(
            f"\n\nGenerated n: {public_key[0]}\n\nGenerated e: {public_key[1]}\n\nGenerated d: {private_key}"
        )
        return Key(public_key, int(private_key), nbits)
