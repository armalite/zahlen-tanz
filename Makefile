.PHONY: venv install run clean gui-setup

# Directory for the virtual environment
VENV_DIR := venv
PYTHON := python3

# Install system-level dependencies
gui-setup:
	sudo apt update && sudo apt install -y libgl1-mesa-glx libglib2.0-0 x11-apps

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && pip install --upgrade pip setuptools wheel

# Install Python dependencies
install: gui-setup venv
	. $(VENV_DIR)/bin/activate && pip install .

# Run the Python script
run: install
	. $(VENV_DIR)/bin/activate && python zahlen.py

# Clean up the environment
clean:
	rm -rf $(VENV_DIR) build dist *.egg-info __pycache__ .pytest_cache
