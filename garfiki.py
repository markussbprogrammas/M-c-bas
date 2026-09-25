import matplotlib.pyplot as plt
import numpy as np
def linijas (a, b):
    ypoints = np.array(np.random.randint(100, size=(a)))
    ypoints2 = np.array(np.random.randint(100, size=(b)))
    ypoints3 = np.array(np.random.randint(100, size=(b)))
    ypoints4 = np.array(np.random.randint(100, size=(b)))
    ypoints5 = np.array(np.random.randint(100, size=(b)))
    plt.plot(ypoints, 'o-.')
    plt.plot(ypoints2, '+:r')
    plt.show()

a = int(input("Ievadiet  a koeficientu?"))
b = int(input("Ievadiet  b koeficientu?"))
c = int(input("Ievadiet  c koeficientu?"))

linijas(a, b)