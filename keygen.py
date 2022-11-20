import primegen

bits = 8
primegen.generate_prime(bits)

p = primegen.generate_prime(bits)
q = primegen.generate_prime(bits)

n = p*q

def carmichael_totient(p, q):
    def gcd(a, b):
        while(b):
            a, b = b, a%b
        return a
    def lcm(a, b):
        return (a*b)/gcd(p, q)
    
    return lcm(p-1, q-1)

