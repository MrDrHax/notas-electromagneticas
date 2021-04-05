import numpy as np
import matplotlib.pyplot as plt

gridSize = int(input("limits of grid\n>>> "))

x, y = np.meshgrid(np.linspace(-gridSize,gridSize,gridSize*2+1), np.linspace(-gridSize,gridSize,gridSize*2+1))

chargesCords = []

amountOfCharges = int(input("Charges count\n>>> "))

E_x = 0
E_y = 0

for i in range (amountOfCharges):
    chargesCords.append((int(input(f"Charge {i} x pos\n>>> ")), int(input(f"Charge {i} y pos\n>>> "))))
    q = int(input(f"Charge for {i}\n>>> ")) 
    E_x += q*(x - chargesCords[i][0]) / (np.sqrt((x - chargesCords[i][0])**2 + (y - chargesCords[i][1])**2))**3
    E_y += q*(y - chargesCords[i][1]) / (np.sqrt((x - chargesCords[i][0])**2 + (y - chargesCords[i][1])**2))**3

    plt.scatter(chargesCords[i][0],chargesCords[i][1])

plt.quiver(x, y, E_x, E_y)
plt.show()