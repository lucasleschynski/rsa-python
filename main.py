from utils.prime_generator import PrimeGenerator
from key_generator import KeyGenerator


def main():
    pg = PrimeGenerator()
    kg = KeyGenerator()
    kg.generate_key(1024)


if __name__ == "__main__":
    main()
