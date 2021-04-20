from operator import mul
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button

figSize = 2

ax = plt.figure().add_subplot(projection='3d')

# Hacer el grid
x, y, z = np.meshgrid(np.linspace(figSize * -1, figSize, figSize * 3 + 1),
                      np.linspace(figSize * -1, figSize, figSize * 3 + 1),
                      np.linspace(figSize * -1, figSize, figSize * 3 + 1))

q1 = 1*10**(-9) # carga 1
q2 = -1*10**(-9) # carga 2

# pos default de las cargas en x
Q_x1 = 1

N = 13  # número de cargas

def calcularTabla(N, q1, q2, Q_x1, Q_x2, chargeSize1, chargeSize2, ax):
    k = 9*10**9   # constante de Coulomb

    Q_y1 = np.linspace(chargeSize1 * -1, chargeSize1, N)
    Q_y2 = np.linspace(chargeSize2 * -1, chargeSize2, N)

    Q_z1 = np.linspace(chargeSize1 * -1, chargeSize1, N)
    Q_z2 = np.linspace(chargeSize2 * -1, chargeSize2, N)

    # calculos que van a cambiar
    E_x = 0
    E_y = 0
    E_z = 0

    # calculos (k*q1*(xm - Q_x1) / r1**3)
    for i in range(N):
        for j in range(N):
            E_x += k*q1*(x - Q_x1) / (np.sqrt((x - Q_x1)**2 + (y - Q_y1[j])**2) + (z - Q_z1[i])**2) ** 3
            E_x += k*q2*(x - Q_x2) / (np.sqrt((x - Q_x2)**2 + (y - Q_y2[j])**2) + (z - Q_z2[i])**2) ** 3

            E_y += k*q1*(y - Q_y1[j]) / (np.sqrt((x - Q_x1)**2 + (y - Q_y1[j])**2) + (z - Q_z1[i])**2) ** 3
            E_y += k*q2*(y - Q_y2[j]) / (np.sqrt((x - Q_x2)**2 + (y - Q_y2[j])**2) + (z - Q_z2[i])**2) ** 3

            E_z += k*q1*(z - Q_z1[i]) / (np.sqrt((x - Q_x1)**2 + (y - Q_y1[j])**2) + (z - Q_z1[i])**2) ** 3
            E_z += k*q2*(z - Q_z2[i]) / (np.sqrt((x - Q_x2)**2 + (y - Q_y2[j])**2) + (z - Q_z2[i])**2) ** 3

        # agregando el punto
        ax.scatter(Q_x1, Q_y1, Q_z1[i], color = "red")
        ax.scatter(Q_x2, Q_y2, Q_z2[i], color = "blue")

    return E_x, E_y, E_z

# ajustando el plot para hacer espacio
plt.subplots_adjust(left=0.25, right=0.75, bottom=0.25)

axcolorBlue = "blue"
axcolorRed = "red"

axSeparation = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolorBlue)
separation_slider = Slider(
    ax=axSeparation,
    label='Separacion',
    valmin=0.1,
    valmax=2,
    valinit=Q_x1,
    orientation="horizontal"
)

axPointValue= plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolorBlue)
pointValue_slider = Slider(
    ax=axPointValue,
    label='N',
    valmin=1,
    valmax=50,
    valinit=10,
    valstep = 1
)

# Make a vertically oriented slider to control the charges and sizes
axSize1 = plt.axes([0.1, 0.25, 0.0225, 0.63], facecolor=axcolorRed)
size1_slider = Slider(
    ax=axSize1,
    label="Size",
    valmin=1,
    valmax=3,
    valinit=2,
    orientation="vertical"
)

axSize2 = plt.axes([0.9, 0.25, 0.0225, 0.63], facecolor=axcolorBlue)
size2_slider = Slider(
    ax=axSize2,
    label="Size",
    valmin=1,
    valmax=3,
    valinit=2,
    orientation="vertical"
)

axCharge1 = plt.axes([0.2, 0.25, 0.0225, 0.63], facecolor=axcolorRed)
charge1_slider = Slider(
    ax=axCharge1,
    label="Charge",
    valmin=1*10**(-9),
    valmax=10*10**(-9),
    valinit=1*10**(-9),
    orientation="vertical"
)

axCharge2 = plt.axes([0.8, 0.25, 0.0225, 0.63], facecolor=axcolorBlue)
charge2_slider = Slider(
    ax=axCharge2,
    label="Charge",
    valmin=-10*10**(-9),
    valmax=-1*10**(-9),
    valinit=-1*10**(-9),
    orientation="vertical"
)

# The function to be called anytime a slider's value changes
def update(val = None):
    ax.clear()

    E_x, E_y, E_z = calcularTabla(pointValue_slider.val, charge1_slider.val, charge2_slider.val, separation_slider.val, separation_slider.val * -1, size1_slider.val, size2_slider.val, ax)

    ax.quiver(x, y, z, E_x, E_y, E_z, length=0.001, normalize=False)

    ax.set_xlim(figSize * -1, figSize)
    ax.set_ylim(figSize * -1, figSize)
    ax.set_zlim(figSize * -1, figSize)
    
    plt.canvas.draw_idle()

# register the update function with each slider
separation_slider.on_changed(update)
size1_slider.on_changed(update)
size2_slider.on_changed(update)
charge1_slider.on_changed(update)
charge2_slider.on_changed(update)

plt.show()