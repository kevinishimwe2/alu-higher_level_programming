# Python - Inheritance

A project exploring object-oriented programming concepts in Python, specifically class inheritance, method overriding, and instance validation.

## Learning Objectives

By the end of this project, you should be able to explain:

- What a superclass, base class, or parent class is
- What a subclass is
- How to list all attributes and methods of a class or instance
- How to inherit a class from another
- How to define a class with multiple base classes
- What the default class every class inherits from is (`object`)
- How to override a method or attribute inherited from a base class
- The purpose of inheritance
- When and how to use `isinstance`, `issubclass`, `type`, and `super`

## Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS
- `pycodestyle` version 2.7.*
- All files must be executable and end with a new line
- First line of every script: `#!/usr/bin/python3`
- All modules, classes, and functions must have docstrings

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Returns a list of available attributes and methods of an object |
| `1-my_list.py` | `MyList` class that inherits from `list` with a `print_sorted()` method |
| `2-is_same_class.py` | Returns `True` if object is exactly an instance of the specified class |
| `3-is_kind_of_class.py` | Returns `True` if object is an instance of, or inherited from, the specified class |
| `4-inherits_from.py` | Returns `True` if object is an instance of a class that inherited (directly or indirectly) from the specified class |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` class with unimplemented `area()` method |
| `7-base_geometry.py` | `BaseGeometry` with `area()` and `integer_validator()` methods |
| `8-rectangle.py` | `Rectangle` class inheriting from `BaseGeometry` with private width and height |
| `9-rectangle.py` | Full `Rectangle` class with `area()` and `__str__()` |
| `10-square.py` | `Square` class inheriting from `Rectangle` (prints as `[Rectangle]`) |
| `11-square.py` | `Square` class with its own `[Square]` string representation |

## Usage Examples

### Lookup (Task 0)
```python
lookup = __import__('0-lookup').lookup
print(lookup(int))   # returns list of all int attributes/methods
```

### MyList (Task 1)
```python
MyList = __import__('1-my_list').MyList
my_list = MyList([3, 1, 2])
my_list.print_sorted()  # prints [1, 2, 3]
print(my_list)          # prints [3, 1, 2] — original unchanged
```

### Class Checkers (Tasks 2–4)
```python
is_same_class(1, int)       # True  — exact match only
is_same_class(1, object)    # False — int inherits from object, but isn't object

is_kind_of_class(1, int)    # True
is_kind_of_class(1, object) # True  — includes parent classes

inherits_from(True, int)    # True  — bool is a subclass of int
inherits_from(True, bool)   # False — True IS a bool, not a subclass of bool
```

### BaseGeometry (Tasks 5–7)
```python
bg = __import__('7-base_geometry').BaseGeometry()
bg.integer_validator("width", 10)   # passes silently
bg.integer_validator("age", 0)      # raises ValueError
bg.integer_validator("name", "hi")  # raises TypeError
bg.area()                           # raises Exception: area() is not implemented
```

### Rectangle & Square (Tasks 8–11)
```python
r = Rectangle(3, 5)
print(r)        # [Rectangle] 3/5
print(r.area()) # 15

s = Square(13)
print(s)        # [Square] 13/13
print(s.area()) # 169
```

## Running Tests

```bash
python3 -m doctest ./tests/*
```

## Key Concepts

### `type()` vs `isinstance()`
- `type(obj) is MyClass` → **exact** class match, returns `False` for subclasses
- `isinstance(obj, MyClass)` → matches the class **and all subclasses**

### Why `type(value) is not int` in `integer_validator`
Since `bool` is a subclass of `int` in Python, `isinstance(True, int)` returns `True`. Using `type(value) is not int` correctly rejects boolean values.

### Class Hierarchy in this Project
```
object
  └── BaseGeometry
        └── Rectangle
              └── Square
```

## Author

Project by Guillaume — ALU Higher Level Programming
