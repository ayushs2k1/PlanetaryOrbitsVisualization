# Planetary Orbits Visualization

This project visualizes the orbits of planets using 3D plotting with the help of orbital parameters from [Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html)

## Features

- 3D visualization of planetary orbits which includes interactive features such as hover and click events to display planetary information and control the animation.
- Dynamic plot title updating with the current date during animation.

## Calculation Details

### Orbital Calculation
The orbits of the planets are calculated using Kepler's laws of planetary motion. Each planet's orbit is defined by several parameters including the perihelion distance (closest approach to the Sun), aphelion distance (farthest distance from the Sun), and orbital period.
 
- Major and Minor Axes Calculation
  - The semi-major axis a and semi-minor axis b of the elliptical orbit are calculated using the orbital eccentricity, perihelion (rmin) and aphelion (rmax) distances
- Solving Kepler's Equation
  - Kepler's equation relates the mean anomaly M, eccentric anomaly E, and orbital eccentricity e. Solving Kepler's equation involves iteratively finding E such that $\ 𝑀 = 𝐸 − 𝑒 sin(𝐸)$ <br>
    where:
    - M is the mean anomaly, calculated as $\ 𝑀 = 2𝜋𝑡/𝑃$ <br>
      where
      - t is the time since perihelion and
      - P is the orbital period.
      - E is the eccentric anomaly.
      - e is the orbital eccentricity.
      - epsilon is the convergence criterion for the iterative solution.
- Position Calculation
  - Using the eccentric anomaly E, the true anomaly θ, and the distance r are calculated as follows:
    $\ θ=2arctan(\sqrt{(1−e) \over (1+e)} tan E/2)$ <br>
    $\ r=a(1−ecosE)$ <br>
    where
    - θ(true anomaly) is the angle between the direction of periapsis and the current position of the planet.
    - r is the distance from the Sun at a given point in time.
    - t is the time since perihelion.
    - P is the orbital period.
- Planetary Movement
  - The position of each planet at a given time is calculated by determining the time elapsed since the planet's last perihelion. This time is then used to calculate the planet's current position in its orbit.

## Example
On a given date, comparing with [Nasa Simulation](https://eyes.nasa.gov/apps/solar-system/#/home?rate=3&time=2024-07-27T17:17:00.949+00:00) gives similar results:
<img width="1303" alt="PlanetOrbit" src="https://github.com/user-attachments/assets/6c8a96d5-c3e0-4138-a77c-feeed38b2d74">

Here's the 3d Simulation:


https://github.com/user-attachments/assets/34a05bf2-1e73-401c-a7dd-3bf43e23ad58

## Project Structure
```
PlanetaryOrbitsVisualization/
├── model.py        # Contains functions to draw orbits and planets
├── view.py         # Sets up the plot and handles user interactions
├── controller.py   # Contains logic for orbit calculations
├── requirements.txt # Lists the dependencies
└── README.md       # Project documentation
```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/ayushs2k1/PlanetaryOrbitsVisualization.git
   cd PlanetaryOrbitsVisualization
   ```
2. Create and activate a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
4. Run the main script to visualize the planetary orbits
   ```
   python3 view.py
   ```
