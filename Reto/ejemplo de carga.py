import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.linspace(-5,5,11), np.linspace(-5,5,11))

Q_x1 = 3 
Q_y1 = 3 
Q_x2 = -3 
Q_y2 = -3

k = 9 * 10 ** 9   # constante de Coulomb
q_1 = 5 * 10 ** -9   # pico Coulombs
q_2 = -3 * 10 ** -9   # pico Coulombs

E_x = k*q_1*(x - Q_x1) / (np.sqrt((x - Q_x1)**2 + (y - Q_y1)**2))**3 + k*q_2*(x - Q_x2) / (np.sqrt((x - Q_x2)**2 + (y - Q_y2)**2))**3 
E_y = k*q_1*(y - Q_y1) / (np.sqrt((x - Q_x1)**2 + (y - Q_y1)**2))**3 + k*q_2*(y - Q_y2) / (np.sqrt((x - Q_x2)**2 + (y - Q_y2)**2))**3

plt.quiver(x, y, E_x, E_y)
plt.show()