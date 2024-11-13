.PHONY: venv install run clean

# Directory for the virtual environment
VENV_DIR := venv
PYTHON := python3

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && pip install --upgrade pip setuptools wheel

# Install dependencies into the virtual environment
install: venv
	. $(VENV_DIR)/bin/activate && pip install .

# Run a Python script within the virtual environment
run: install
	. $(VENV_DIR)/bin/activate && python rossler_4d.py

# Clean up virtual environment and other build artifacts
clean:
	rm -rf $(VENV_DIR) build dist *.egg-info __pycache__ .pytest_cache
