from secrets import randbelow

import matplotlib.pyplot as plt
import numpy as np


def cycle_attack(cycles, q):
    alice_blocks = []
    for _ in range(cycles):
        block = 0
        h = 0
        for i in range(3):
            rdm_val = randbelow(101)
            if rdm_val <= q:  # the attacker minning a block
                block += 1
                h += 1
            elif i == 0 and rdm_val > q:  # honest miners minning the first block
                h = 1
                break
        if block == 1:  # if the attacker has mined only one block, he/she wins nothing
            h = 2
            block = 0
        alice_blocks.append((block, h))
    return alice_blocks


def main():
    rewards = [p / 10 for p in range(0, 500, 2)]
    nbr_cycles = 1000

    result = [[x for x in cycle_attack(nbr_cycles, p)] for p in rewards]
    value = [sum(num for num, den in x)/sum(den for num, den in x) for x in result]
    rewards = [p / 100 for p in rewards]
    plt.title("Simulation 1 + 2 attack")
    plt.plot(rewards, value, label="honest yield calculate ")
    plt.plot(np.linspace(0, 0.5, 100), np.linspace(0, 0.5, 100), label="theorical yield")
    plt.legend(loc='upper left')
    plt.show()
main()
