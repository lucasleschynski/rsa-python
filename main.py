import functools
from utils.prime_generator import PrimeGenerator
from key_generator import KeyGenerator
from codec import EncryptingCodec as codec


def main():
    pg = PrimeGenerator()
    kg = KeyGenerator()
    alice = kg.generate_key(1024)
    bob = kg.generate_key(1024)

    message = 123456789123456789
    print(f"Message is {message.bit_length()} bits")

    c = codec.encrypt_message(message, alice.public_key)
    print(f"Encrypted message: {c}")

    m = codec.decrypt_message(c, alice)
    print(f"Decrypted message: {m}")


if __name__ == "__main__":
    main()
