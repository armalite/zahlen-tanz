# Zahlen Tanz
Kurven, die tanzen. Zahlen, die leben. Python macht’s möglich.

## Requirements
Before setting up the project, ensure the following dependencies are installed on your system:
  * Python 3.10+: Download Python from the official website.
  * Tkinter:
    * Linux: Install python3-tk via your package manager (e.g., sudo apt install python3-tk).
    * macOS: Install Python with tcl-tk support (e.g., brew install python-tk).
    * Windows: Tkinter is included by default with the Python installer.

## Setup Instructions
1. Clone the Repository:
```bash
git clone https://github.com/armalite/zahlen-tanz.git
cd zahlen-tanz
```

2. Install the Project:
```bash
make install
```

This will:

 * Set up a virtual environment.
 * Install all required Python dependencies.

3. Run the Script:
```bash
make run
```

## Caveats and Troubleshooting
### Missing tkinter
If you encounter a ModuleNotFoundError: `No module named 'tkinter', ensure tkinter is installed:`

 * On Linux:
```bash
sudo apt install python3-tk
```
 * On macOS:
```bash
brew install python-tk
```

### Test if tkinter is working by running:
```bash
python3 -m tkinter
```
A small GUI window should appear.

### Slow Animation
The animation is optimized for speed by skipping frames and reducing the delay between frames. If it still feels slow, you can tweak the frames and interval parameters in the script:
```python
ani = FuncAnimation(
fig,
update,
frames=range(0, len(t_eval), 3),
interval=5,
blit=True
)
```

### Mac-Specific Backend Issues
If the animation doesn’t display properly on macOS, ensure you have Python installed with tcl-tk support, and try switching the matplotlib backend to macosx:
```python
import matplotlib
matplotlib.use("macosx")
```

### Exiting the Animation
Use the "Quit" button in the tkinter GUI to stop the animation and close the application.
If the process doesn’t exit cleanly, you can kill it manually:
```bash
pkill -9 python
```