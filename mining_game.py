# a: blocks mined in advance by the attacker
# h: blocks mined in advance by the bank
# n: number of remaining actions

import functools

a = 0
h = 0
n = 400
@functools.cache
def E (a, h, n, q, c): 
    if n == 0:
        return 0

    if a > h:
        return max(((h+1) - c + E(a-h-1, 0, n-1, q, c)),
                    (q * E(a+1, h, n-1, q, c) + (1-q) * (E(a, h+1, n-1, q, c) - c)))

    if a <= h:
        return max(E(0, 0, n-1, q, c),
                    (q * E(a+1, h, n-1, q, c) + (1-q) * (E(a, h +1, n-1, q, c) - c)))


q4 = 0.10 # non profitable
q3 = 0.20 # non profitable
q = 0.3293929 #limite a partir de laquelle il est rentable d'attaquer
q1 = 0.40 #l'attaquant est rentable
q2 = 0.50 # l'attaquant est rentable