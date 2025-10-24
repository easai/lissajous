import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Parameters for Lissajous curve
A = 1      # amplitude in x
B = 1      # amplitude in y
a = 3      # frequency in x
b = 2      # frequency in y
delta = np.pi / 2  # phase difference

# Generate time values
t = np.linspace(0, 2 * np.pi, 300)

# Parametric equations
x = A * np.sin(a * t + delta)
y = B * np.sin(b * t)

# Use distance from origin as color scale
scale = np.sqrt(x**2 + y**2)

# Plot using seaborn
sns.scatterplot(x=x, y=y, hue=scale, palette='pastel', legend=False, s=100)
plt.title("Lissajous Curve Colored by Distance from Origin")
plt.axis('equal')
plt.grid(True)
plt.show()