# Python - import & modules

This project covers importing functions and variables from other Python files, using modules, and working with command line arguments.

## Learning Objectives

- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code from being executed when imported (using `if __name__ == "__main__":`)
- How to use command line arguments with Python programs

## Project Files

- `0-add.py` - Imports add function and prints the result of addition
- `1-calculation.py` - Imports calculator functions and performs operations
- `2-args.py` - Prints the number and list of command line arguments
- `3-infinite_add.py` - Adds all command line arguments
- `4-hidden_discovery.py` - Prints names defined in a compiled module
- `5-variable_load.py` - Imports and prints a variable from another file

## Supporting Files

- `add_0.py` - Module containing add function
- `calculator_1.py` - Module containing math operation functions
- `variable_load_5.py` - Module containing a variable
- `hidden_4.pyc` - Compiled Python module (download separately)

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- pycodestyle version 2.7.*
- All files must be executable
- All files must start with `#!/usr/bin/python3`

## Usage

### Task 0 - Import a simple function
```bash
./0-add.py
```

### Task 1 - Calculator
```bash
./1-calculation.py
```

### Task 2 - Command line arguments
```bash
./2-args.py Hello Welcome To Python
```

### Task 3 - Infinite addition
```bash
./3-infinite_add.py 79 10 -40 -300 89
```

### Task 4 - Hidden discovery
First download the hidden module:
```bash
curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
```
Then run:
```bash
./4-hidden_discovery.py | sort
```

### Task 5 - Variable load
```bash
./5-variable_load.py
```

## Author

ALU Student - Higher Level Programming Project
