# Python - Input/Output

A project covering file handling and JSON serialization/deserialization in Python.

## Learning Objectives

- How to open, read, write, and append to files using `with`
- How to read a file line by line and move the cursor
- What JSON is and how to serialize/deserialize Python objects
- How to convert between Python data structures and JSON strings

## Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS
- `pycodestyle` version 2.7.*
- All files executable, ending with a newline
- First line: `#!/usr/bin/python3`
- All modules and functions must have docstrings

## Files

| File | Description |
|------|-------------|
| `0-read_file.py` | Reads a UTF8 text file and prints it to stdout |
| `1-write_file.py` | Writes a string to a file, returns character count |
| `2-append_write.py` | Appends a string to a file, returns character count |
| `3-to_json_string.py` | Returns the JSON string representation of an object |
| `4-from_json_string.py` | Returns a Python object from a JSON string |
| `5-save_to_json_file.py` | Saves a Python object to a file as JSON |
| `6-load_from_json_file.py` | Creates a Python object from a JSON file |
| `7-add_item.py` | Adds CLI arguments to a persistent JSON list file |
| `8-class_to_json.py` | Returns `__dict__` of an object for JSON serialization |
| `9-student.py` | `Student` class with `to_json()` method |
| `10-student.py` | `Student` class with filtered `to_json(attrs)` |
| `11-student.py` | `Student` class with `to_json` and `reload_from_json` |
| `12-pascal_triangle.py` | Returns Pascal's triangle as a list of lists |

## Usage Examples

### File I/O (Tasks 0–2)
```python
read_file("my_file.txt")                        # prints contents
n = write_file("out.txt", "Hello!\n")           # returns 7
n = append_write("out.txt", "More text\n")      # returns 10
```

### JSON (Tasks 3–6)
```python
to_json_string([1, 2, 3])       # '[1, 2, 3]'
from_json_string('[1, 2, 3]')   # [1, 2, 3]
save_to_json_file(obj, "f.json")
obj = load_from_json_file("f.json")
```

### Add Items Script (Task 7)
```bash
./7-add_item.py Best School     # saves ["Best", "School"] to add_item.json
./7-add_item.py 89 Python C     # appends, saves ["Best", "School", "89", "Python", "C"]
```

### Student (Tasks 9–11)
```python
s = Student("John", "Doe", 23)
s.to_json()                         # {'first_name': 'John', 'last_name': 'Doe', 'age': 23}
s.to_json(['first_name', 'age'])    # {'first_name': 'John', 'age': 23}
s.reload_from_json({'age': 30})     # updates s.age to 30
```

### Pascal's Triangle (Task 12)
```python
pascal_triangle(5)
# [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
pascal_triangle(0)  # []
```

## Running Tests
```bash
python3 -m doctest ./tests/*
```

## Author

Project by Guillaume — ALU Higher Level Programming
