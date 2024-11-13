import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Parameters for the generalized Rössler attractor
a, b, c, d = 0.2, 0.2, 5.7, 1.0

# Define the Rössler system in 4D
def rossler_4d(t, state):
    x, y, z, w = state
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    dw = -d * w + x * y
    return [dx, dy, dz, dw]

# Initial conditions and time span
init_state = [1.0, 1.0, 1.0, 1.0]
t_span = (0, 100)
t_eval = np.linspace(0, 100, 10000)

# Solve the system
solution = solve_ivp(rossler_4d, t_span, init_state, t_eval=t_eval)
x, y, z, w = solution.y

# Create a tkinter root window
root = tk.Tk()
root.title("4D Rössler Attractor Animation")

# Create the matplotlib figure and axis with a black background
fig = plt.figure(figsize=(8, 6), facecolor='black')  # Set figure background to black
ax = fig.add_subplot(111, projection="3d", facecolor='black')  # Set 3D plot background to black
ax.set_xlim((-15, 15))
ax.set_ylim((-15, 15))
ax.set_zlim((-5, 25))

# Remove chart elements for a cleaner visualization
ax.set_axis_off()  # Turns off axis lines, ticks, and labels

# Initialize the line for the animation with a color gradient
line, = ax.plot([], [], [], lw=2, color='cyan')  # Initial line color

# Animation update function with changing colors
def update(frame):
    # Update the line data
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    
    # Change line color dynamically for a gradient effect
    line.set_color(plt.cm.plasma(frame / len(t_eval)))  # Color changes with frame
    return line,

# Faster animation with skipping frames and reduced delay
ani = FuncAnimation(
    fig,
    update,
    frames=range(0, len(t_eval), 3),  # Skip every 3 frames
    interval=5,  # Reduce delay between frames
    blit=True    # Enable optimized rendering
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
