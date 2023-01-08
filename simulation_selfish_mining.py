from random import *
import numpy as np
import matplotlib.pyplot as plt

def X() -> np.ndarray:
    return np.linspace(0, 0.5, 100)



BLOCK_TIME =600
BLOCK_REWARD = 6.25

def simulation_selfish_mining(n, q, gamma) -> (float, int):
    reward = 0
    time = 0
    i = 0
    
    while i < int(n):
        i += 1
        stop = False
        block = 0
        while not stop:
            while random() < q:  # l'attaquant mine un block
                block += 1
                time += BLOCK_TIME
            if block >= 2:  # l'attaquant écrase la blockchain officielle
                block -= 2
                reward += 2 * BLOCK_REWARD
            elif block == 1 and random() > q:  # l'attaquant perd
                block = 0
                if random() < gamma:  # il tente de diffuser son block aux grace a sa connectivité
                    reward += BLOCK_REWARD
            elif block == 0:  # l'attaquant est en retard
                time += BLOCK_TIME
            stop = block == 0
    return reward, time


def main():
    cycles = input("How many attack do you wish to simulate ? (1<x<10001) : ")
    connectivity = float(20)/100
    # Practical dishonest yield
    x, y = X(), []
    for q in x:
        R, T = simulation_selfish_mining(cycles, q, connectivity)
        y.append(R / T*100)
    # Theoretical honest yield
    x1, y1 = X(), []
    for q in x:
        y1.append(q * BLOCK_REWARD / BLOCK_TIME*100)

    bascule = 0
    i = 0
    while bascule==0 and i<len(x):
        m = max(y[i], y1[i])
        if m == y[i]:
            bascule = m
        i += 1
    
    plt.plot(x, y, label="Practical dishonest yield")
    plt.plot(x1, y1, label="Theoretical honest yield")
    plt.legend(loc='upper left')
    plt.title("Simulation selfish mining")
    plt.grid()
    plt.show()
main()
