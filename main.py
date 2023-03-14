from utils.prime_generator import PrimeGenerator
from key_generator import KeyGenerator
from codec import EncryptingCodec as codec


def main():
    # TODO: implement threading for key generation
    pg = PrimeGenerator()
    kg = KeyGenerator()
    alice = kg.generate_key(2048)
    bob = kg.generate_key(2048)

    message_string = input("Enter a message to encrypt: ")
    message = codec.encode_message(message_string)
    print(f"Message is {message.bit_length()} bits")

    c = codec.encrypt_message(message, alice.public_key)
    print(f"Encrypted message: {c}")

    m = codec.decrypt_message(c, alice)
    print(f"Decrypted message as int: {m}")

    decrypted = codec.decode_message(m)
    print(f"Decoded message: {decrypted}")


if __name__ == "__main__":
    main()
