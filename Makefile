# Variables
PYTHON := python3
VENV := venv
SRC_DIR := pythonproject/src
TEST_DIR := pythonproject/tests
REQUIREMENTS := requirements.txt

# Phony targets
.PHONY: all venv install test format lint clean

# Default target
all: venv install test format lint

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)

# Install project dependencies
install: venv
	$(VENV)/bin/pip install --upgrade pip -r  $(REQUIREMENTS)

# Run unit tests
test: 
	$(VENV)/bin/pytest $(TEST_DIR)
	$(VENV)/bin/pytest --nbval-lax $(SRC_DIR)
	# nbval doesnt handle a strict test for formatted jupyter outputs well

# Format code with Black
format:
	$(VENV)/bin/black $(SRC_DIR)

# Lint code with Ruff
lint:
	$(VENV)/bin/ruff check $(SRC_DIR)

# Clean up generated files and virtual environment
clean:
	rm -rf $(VENV) __pycache__ .pytest_cache
