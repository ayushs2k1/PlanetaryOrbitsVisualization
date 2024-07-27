import numpy as np
from numpy import cos, sin
from controller import SolveOrbit
from datetime import datetime

initial_date = datetime(2024, 7, 27)

orbital_data = {
    'Mercury': {'rmin': 46.000, 'rmax': 69.818, 'angle': 7.004, 'P': 87.969},
    'Venus': {'rmin': 107.480, 'rmax': 108.941, 'angle': 3.395, 'P': 224.695},
    'Earth': {'rmin': 147.095, 'rmax': 152.100, 'angle': 0.0, 'P': 365.256},
    'Mars': {'rmin': 206.650, 'rmax': 249.261, 'angle': 1.848, 'P': 686.980},
    'Jupiter': {'rmin': 740.595, 'rmax': 816.363, 'angle': 1.304, 'P': 4332.59},
}

perihelion_dates = {
    'Mercury': datetime(2024, 5, 15),
    'Venus': datetime(2024, 1, 4),
    'Earth': datetime(2023, 1, 4),
    'Mars': datetime(2022, 6, 21),
    'Jupiter': datetime(2023, 1, 20),
}

planet_data = {
    'Mercury': {
        'Distance from Sun': '57.91 million km', 'Orbital Period': '87.97 days', 'Eccentricity': '0.2056',
        'Perihelion': '46.00 million km', 'Aphelion': '69.82 million km', 'Mean Velocity': '47.87 km/s',
        'Max Velocity': '60.00 km/s', 'Min Velocity': '35.00 km/s', 'Rotation Period': '58.6 days'
    },
    'Venus': {
        'Distance from Sun': '108.2 million km', 'Orbital Period': '224.7 days', 'Eccentricity': '0.0068',
        'Perihelion': '107.48 million km', 'Aphelion': '108.94 million km', 'Mean Velocity': '35.02 km/s',
        'Max Velocity': '36.00 km/s', 'Min Velocity': '34.00 km/s', 'Rotation Period': '243.0 days'
    },
    'Earth': {
        'Distance from Sun': '149.6 million km', 'Orbital Period': '365.26 days', 'Eccentricity': '0.0167',
        'Perihelion': '147.10 million km', 'Aphelion': '152.10 million km', 'Mean Velocity': '29.78 km/s',
        'Max Velocity': '30.29 km/s', 'Min Velocity': '29.29 km/s', 'Rotation Period': '24.0 hours'
    },
    'Mars': {
        'Distance from Sun': '227.9 million km', 'Orbital Period': '687 days', 'Eccentricity': '0.0934',
        'Perihelion': '206.65 million km', 'Aphelion': '249.26 million km', 'Mean Velocity': '24.07 km/s',
        'Max Velocity': '25.00 km/s', 'Min Velocity': '23.00 km/s', 'Rotation Period': '24.6 hours'
    },
    'Jupiter': {
        'Distance from Sun': '778.6 million km', 'Orbital Period': '4332.59 days', 'Eccentricity': '0.0487',
        'Perihelion': '740.60 million km', 'Aphelion': '816.36 million km', 'Mean Velocity': '13.06 km/s',
        'Max Velocity': '13.72 km/s', 'Min Velocity': '12.44 km/s', 'Rotation Period': '9.93 hours',
        'Day Length': '9.93 hours', 'Obliquity': '3.13 degrees', 'Inclination': '1.30 degrees'
    },
}

def draw_orbits(ax):
    for planet, data in orbital_data.items():
        theta = np.linspace(0, 2 * np.pi, 200)  # Reduce the number of points
        x = data['rmax'] * np.cos(theta)
        y = data['rmin'] * np.sin(theta)
        z = np.zeros_like(theta)
        ax.plot(x, y, z, color='grey', alpha=0.5)  # Added transparency

def draw_planet(ax, name, rmax, rmin, t, P):
    SCALE = 1e6  # Using 10^6 km for scaling
    theta, r = SolveOrbit(rmax * SCALE, rmin * SCALE, t, P)
    x = -r * cos(theta) / SCALE
    y = r * sin(theta) / SCALE
    z = 0  # for simplicity, setting all orbits on the xy-plane
    planet = ax.scatter(x, y, z, color='blue', s=50, label=name, picker=True)
    label = ax.text(x, y, z + 20, name, fontsize=8, ha='center', color='black', animated=True)
    return planet, label
