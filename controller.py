from math import sin, cos, pi, atan2, sqrt

def time_since_perihelion(current_date, perihelion_date):
    delta = current_date - perihelion_date
    return delta.total_seconds() / (60 * 60 * 24)  # convert to days

def OrbitLength(M, m):
    a = (M + m) / 2
    c = a - m
    e = c / a
    b = a * (1 - e**2)**0.5
    return 2 * a, 2 * b, e

def solve_kepler(M, e, epsilon=1e-6):
    E = M  # initial guess
    while True:
        delta_E = (M - E + e * sin(E)) / (1 - e * cos(E))
        E += delta_E
        if abs(delta_E) < epsilon:
            break
    return E

def SolveOrbit(rmax, rmin, t, P):
    a = (rmax + rmin) / 2
    e = (rmax - rmin) / (rmax + rmin)
    M = (2 * pi / P) * (t % P)
    E = solve_kepler(M, e)
    theta = 2 * atan2(sqrt(1 + e) * sin(E / 2), sqrt(1 - e) * cos(E / 2))
    r = a * (1 - e * cos(E))
    return theta, r
