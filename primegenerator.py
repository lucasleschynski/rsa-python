import random


class PrimeGenerator:
    def __init__(self):
        pass

    def random_n_bits(self, length):
        """
        Generate random n-bit number.

        Args:
            length (int): Number of bits

        Returns:
            int: random n-bit number with MSB, LSB = 1
        """
        p = random.getrandbits(length)
        # Bitwise mask to set MSB, LSB = 1
        p |= (1 << length - 1) | 1
        return p

    def miller_rabin(self, n, k):
        """
        Miller-Rabin primality test.
        Args:
            n (int): Prime candidate
            k (int): Number of test rounds to be performed

        Returns:
            bool: n is/isn't prime
        """
        if n == 2 or n == 3:
            return True

        if n <= 1 or n % 2 == 0:
            return False

        r = 0
        s = n - 1

        while s % 2 == 0:
            r += 1
            s //= 2
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True

    def generate_prime(self, n):
        """
        Generates n-bit prime.
        """
        while True:
            candidate = self.random_n_bits(n)
            if not self.miller_rabin(candidate, 40):
                continue
            else:
                # print(f"{n} bit prime is: {candidate}")
                return candidate

    def first_n_primes(self, n):
        """
        Generates first n prime numbers.
        (Not actually used)
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
