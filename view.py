import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import timedelta
from controller import time_since_perihelion
from model import draw_orbits, draw_planet, initial_date, orbital_data, perihelion_dates, planet_data
from controller import SolveOrbit
from numpy import cos, sin

# Set up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x10^6 km')
ax.set_ylabel('x10^6 km')
ax.set_zlabel('x10^6 km')
ax.set_xlim(-600, 600)  
ax.set_ylim(-600, 600)
ax.set_zlim(-600, 600)
ax.grid(True)
ax.scatter(0, 0, 0, s=150, color='y')  # Sun
ax.text(0, 0, 50, 'Sun', fontsize=12, ha='center', color='black')

# Draw orbits
draw_orbits(ax)

# Create dictionaries to hold planet artists and labels for updating
planet_artists = {}
planet_labels = {}
for planet, data in orbital_data.items():
    t = time_since_perihelion(initial_date, perihelion_dates[planet])
    planet_artist, label = draw_planet(ax, planet, data['rmax'], data['rmin'], t, data['P'])
    planet_artists[planet] = planet_artist
    planet_labels[planet] = label

# Animation control variables
anim_running = True
animation_speed = 100

# Initialize the annotation for planet details
annotation = ax.annotate('', xy=(0.5, 0.1), xycoords='axes fraction',
                         bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white'),
                         fontsize=10, ha='center', color='black')

def update(frame):
    current_date = initial_date + timedelta(days=frame)
    ax.set_title(f'Planetary Orbits on {current_date.strftime("%Y-%m-%d")}\nClick to pause at the current date\nHover over planets to see orbital parameters')
    for planet, data in orbital_data.items():
        t = time_since_perihelion(current_date, perihelion_dates[planet])
        theta, r = SolveOrbit(data['rmax'] * 1e6, data['rmin'] * 1e6, t, data['P'])
        x = -r * cos(theta) / 1e6
        y = r * sin(theta) / 1e6
        z = 0  # for simplicity, setting all orbits on the xy-plane
        if planet in planet_artists:
            planet_artists[planet]._offsets3d = ([x], [y], [z])
        if planet in planet_labels:
            planet_labels[planet].set_position((x, y))
            planet_labels[planet].set_3d_properties(z + 20)  # Offset for visibility
    return list(planet_artists.values()) + list(planet_labels.values()) + [annotation]

def on_click(event):
    global anim_running
    if anim_running:
        anim.event_source.stop()
        anim_running = False
    else:
        anim.event_source.start()
        anim_running = True

def on_hover(event):
    if event.inaxes == ax:
        for planet, artist in planet_artists.items():
            contains, _ = artist.contains(event)
            if contains:
                info = planet_data[planet]
                info_text = f'{planet}:\n'
                for key, value in info.items():
                    info_text += f'{key}: {value}\n'
                annotation.set_text(info_text)
                fig.canvas.draw_idle()
                break
        else:
            annotation.set_text('')  # Clear annotation if not hovering over any planet

# Create animation
anim = FuncAnimation(fig, update, frames=range(0, 365, 1), interval=animation_speed, blit=False)

# Connect event handlers
fig.canvas.mpl_connect('button_press_event', on_click)
fig.canvas.mpl_connect('motion_notify_event', on_hover)

plt.show()
