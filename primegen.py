import random
import math


def first_n_primes(n):
    """
    Generates first n prime numbers
    for use with low level primality test
    """
    prime_list = [2]
    num = 3

    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        # if it is a prime, then add it to the list
        else:
            prime_list.append(num)
        num += 2
    return prime_list

first_primes_list = first_n_primes(100)

def random_n_bits(n):
    """
    Generates a random number of n bits
    and avoids many trailing zeroes
    """
    maxnum = (2 ** n) - 1
    minnum = (2 ** (n-1)) + 1
    return minnum + random.randint(minnum, maxnum)

print(random_n_bits(32))

def low_level_prime_test(n):
    """
    Divides candidate with small primes -- low level primality test
    """
    while True: 
        prime_candidate = random_n_bits(n)

        for divisor in first_primes_list:
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
            else: 
                return prime_candidate


def miller_rabin(candidate):
    """
    Uses Miller-Rabin primality test to check
    large numbers for primality.
    Probabilistic but effective.
    """
    max_divisions_by_two = 0
    even_component = candidate-1

    while even_component % 2 == 0:
        even_component >>= 1
        max_divisions_by_two += 1
    assert 2**max_divisions_by_two * even_component == candidate-1

    def trial_composite(round_tester):
        if pow(round_tester, even_component, candidate) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(round_tester, 2**i * even_component, candidate) == candidate-1:
                return False
        return True

    # Set number of trials here
    num_trials = 20
    for i in range(num_trials):
        round_tester = random.randrange(2, candidate)
        if trial_composite(round_tester):
            return False
    return True

def generate_prime(n):
    while True:
        candidate = low_level_prime_test(n)
        if not miller_rabin(candidate):
            continue
        else:
            print(f"{n} bit prime is: {candidate}")
            return candidate