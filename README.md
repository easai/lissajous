## Lissajous Curve

This Python script generates and visualizes a Lissajous curve using `seaborn.scatterplot`, with each point colored by its distance from the origin. It’s a vibrant way to explore parametric sine wave interactions and their geometric beauty.

- Generates a 2D Lissajous curve using parametric sine functions.
- Computes the Euclidean distance of each point from the origin.
- Colors each point based on this distance using a perceptually uniform colormap.
- Displays the result using Seaborn and Matplotlib.

### The Lissajous curve

The Lissajous curve is defined by:

$$
x(t) = A \cdot \sin(a t + \delta), \quad y(t) = B \cdot \sin(b t)
$$

Where:
- $ A, B $ are amplitudes
- $ a, b $ are frequencies
- $ \delta $ is the phase difference

### Usage

Install dependencies with:

```bash
poetry install
```

Run the script directly:

```bash
poetry run py src\lissajous\lissajous.py
```

### Customization

You can tweak the parameters A, B, a, b, and delta in the script to explore different curve shapes.
