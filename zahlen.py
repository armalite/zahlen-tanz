import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import cycle

# Parameters for Rössler Attractor
a, b, c, d = 0.2, 0.2, 5.7, 1.0

# Parameters for Lorenz Attractor
sigma, rho, beta = 10, 28, 8 / 3

# Define the Rössler system in 4D
def rossler_4d(t, state):
    x, y, z, w = state
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    dw = -d * w + x * y
    return [dx, dy, dz, dw]

# Define the Lorenz Attractor
def lorenz_attractor(t, state):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

# Initial conditions and time spans
init_state_rossler = [1.0, 1.0, 1.0, 1.0]
init_state_lorenz = [1.0, 1.0, 1.0]
t_span = (0, 50)  # Shorter time span for faster animation
t_eval = np.linspace(0, 50, 5000)  # More dense frames for smoother visuals

# Solve the systems
solution_rossler = solve_ivp(rossler_4d, t_span, init_state_rossler, t_eval=t_eval)
solution_lorenz = solve_ivp(lorenz_attractor, t_span, init_state_lorenz, t_eval=t_eval)

x_r, y_r, z_r, w_r = solution_rossler.y
x_l, y_l, z_l = solution_lorenz.y

# Repeat the data to extend the animation duration
repeats = 10  # Number of times to repeat the data
x_r = np.tile(x_r, repeats)
y_r = np.tile(y_r, repeats)
z_r = np.tile(z_r, repeats)
x_l = np.tile(x_l, repeats)
y_l = np.tile(y_l, repeats)
z_l = np.tile(z_l, repeats)
total_frames = len(t_eval) * repeats

# Create a tkinter root window
root = tk.Tk()
root.title("4D Rössler and Lorenz Attractors")

# Create the matplotlib figure and axes
fig = plt.figure(figsize=(12, 6), facecolor='black')  # Set figure background to black

# Rössler subplot
ax_rossler = fig.add_subplot(121, projection="3d", facecolor='black')
ax_rossler.set_xlim((-15, 15))
ax_rossler.set_ylim((-15, 15))
ax_rossler.set_zlim((-5, 25))
ax_rossler.set_axis_off()  # No axis

# Lorenz subplot
ax_lorenz = fig.add_subplot(122, projection="3d", facecolor='black')
ax_lorenz.set_xlim((-25, 25))
ax_lorenz.set_ylim((-25, 25))
ax_lorenz.set_zlim((0, 50))
ax_lorenz.set_axis_off()  # No axis

# Initialize the lines for animation
line_rossler, = ax_rossler.plot([], [], [], lw=2, color='cyan')  # Rössler line
line_lorenz, = ax_lorenz.plot([], [], [], lw=2, color='lime')  # Lorenz line

# Update function for Rössler
def update_rossler(frame):
    step = 5  # Increase the step size for faster updates
    line_rossler.set_data(x_r[:frame * step], y_r[:frame * step])
    line_rossler.set_3d_properties(z_r[:frame * step])
    # Brighten colors using the Spectral colormap
    line_rossler.set_color(plt.cm.Spectral(frame / total_frames))  # Brighter gradient
    return line_rossler,

# Update function for Lorenz
def update_lorenz(frame):
    line_lorenz.set_data(x_l[:frame], y_l[:frame])
    line_lorenz.set_3d_properties(z_l[:frame])
    # Bright colors using spring colormap
    line_lorenz.set_color(plt.cm.spring(frame / total_frames))  # Bright gradient
    return line_lorenz,

# Combine updates
def update(frame):
    update_rossler(frame)
    update_lorenz(frame)
    return line_rossler, line_lorenz

# Continuous animation
ani = FuncAnimation(
    fig,
    update,
    frames=cycle(range(0, total_frames // 5)),  # Extended duration
    interval=2,  # Reduce delay between frames for quicker animation
    blit=True
)

# Embed the matplotlib figure in tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Add a "Quit" button to close the application
def quit_application():
    root.quit()  # Stops the tkinter mainloop
    root.destroy()  # Destroys the tkinter window

button = tk.Button(root, text="Quit", command=quit_application)
button.pack(side=tk.BOTTOM)

# Run the tkinter main loop
root.mainloop()
