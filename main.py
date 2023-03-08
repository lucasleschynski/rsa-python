import functools
from utils.prime_generator import PrimeGenerator
from key_generator import KeyGenerator
from codec import EncryptingCodec as codec


def main():
    pg = PrimeGenerator()
    kg = KeyGenerator()
    alice = kg.generate_key(16)
    bob = kg.generate_key(16)

    message = 12345

    c = codec.encrypt_message(message, alice.public_key)
    print(f"Encrypted message: {c}")

    m = codec.decrypt_message(c, alice)
    print(f"Decrypted message: {m}")


def carmichael_totient(p: int, q: int) -> int:
    """Performs the carmichael totient function (lambda) on n, or p * q

    Returns:
        int: lambda(n)
    """

    def gcd(a, b):
        while a > 0:
            b = b % a
            (a, b) = (b, a)
        return b

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return lcm(p - 1, q - 1)


if __name__ == "__main__":
    main()
    # print(carmichael_totient(13, 13))
