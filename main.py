import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from math import *
from datetime import datetime

# Define current date
current_date = datetime(2024, 7, 27)

# Define perihelion times for the planets
perihelion_dates = {
    'Mercury': datetime(2024, 5, 15),
    'Venus': datetime(2024, 1, 4),
    'Earth': datetime(2023, 1, 4),
    'Mars': datetime(2022, 6, 21),
    'Jupiter': datetime(2023, 1, 20),
}

# Function to calculate time since perihelion in days
def time_since_perihelion(current_date, perihelion_date):
    delta = current_date - perihelion_date
    return delta.total_seconds() / (60 * 60 * 24)  # convert to days

# Set up plot
fig, ax = plt.subplots()
plt.title(f'Planetary Orbits on {current_date.date()}')
plt.ylabel('x10^6 km')
plt.xlabel('x10^6 km')

# Adjust limits to better fit the orbits
ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)
plt.grid()

# Create the point to represent the Sun at the origin
ax.scatter(0, 0, s=200, color='y')
plt.annotate('Sun', xy=(0, -30))

# Function to calculate orbital elements
def OrbitLength(M, m):
    a = (M + m) / 2
    c = a - m
    e = c / a
    b = a * (1 - e**2)**0.5
    return 2 * a, 2 * b, e

# Function to draw the orbit of a planet
def PlanetOrbit(name, M, m, angle):
    w, h, e = OrbitLength(M, m)
    Xoffset = ((M + m) / 2) - m
    orbit = Ellipse(xy=(Xoffset, 0), width=w, height=h, angle=angle, linewidth=1, fill=False)
    ax.add_artist(orbit)

# Solve Kepler's equation using Newton's method
def solve_kepler(M, e, epsilon=1e-6):
    E = M  # initial guess
    while True:
        delta_E = (M - E + e * sin(E)) / (1 - e * cos(E))
        E += delta_E
        if abs(delta_E) < epsilon:
            break
    return E

# Solve the orbit to find position
def SolveOrbit(rmax, rmin, t, P):
    a = (rmax + rmin) / 2
    e = (rmax - rmin) / (rmax + rmin)
    M = (2 * pi / P) * (t % P)
    E = solve_kepler(M, e)
    theta = 2 * atan2(sqrt(1 + e) * sin(E / 2), sqrt(1 - e) * cos(E / 2))
    r = a * (1 - e * cos(E))
    return theta, r

# Draw the planet at its current position
def DrawPlanet(name, rmax, rmin, t, P):
    SCALE = 1e6  # Using 10^6 km for scaling
    theta, r = SolveOrbit(rmax * SCALE, rmin * SCALE, t, P)
    x = -r * cos(theta) / SCALE
    y = r * sin(theta) / SCALE
    planet = Circle((x, y), 10) 
    ax.add_artist(planet)
    plt.annotate(name, xy=(x, y), fontsize=8, ha='center')

# Orbital data from the table
orbital_data = {
    'Mercury': {'rmin': 46.000, 'rmax': 69.818, 'angle': 7.004, 'P': 87.969},
    'Venus': {'rmin': 107.480, 'rmax': 108.941, 'angle': 3.395, 'P': 224.695},
    'Earth': {'rmin': 147.095, 'rmax': 152.100, 'angle': 0.0, 'P': 365.256},
    'Mars': {'rmin': 206.650, 'rmax': 249.261, 'angle': 1.848, 'P': 686.980},
    'Jupiter': {'rmin': 740.595, 'rmax': 816.363, 'angle': 1.304, 'P': 4332.59},
}

# Plot orbits for all planets
for planet, data in orbital_data.items():
    PlanetOrbit(planet, data['rmax'], data['rmin'], data['angle'])

# Plot positions for all planets
for planet, data in orbital_data.items():
    t = time_since_perihelion(current_date, perihelion_dates[planet])
    DrawPlanet(planet, data['rmax'], data['rmin'], t, data['P'])

plt.show()
