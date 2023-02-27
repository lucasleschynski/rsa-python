from primegenerator import PrimeGenerator


def main():
    pg = PrimeGenerator()
    # print(pg.first_n_primes(100))
    print(pg.generate_prime_candidate(256))


if __name__ == "__main__":
    main()
