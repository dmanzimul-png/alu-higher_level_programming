
---

## Tasks Overview

| Task | File | Description |
|------|------|-------------|
| 0 | `0-lookup.py` | Function `lookup(obj)` returns a list of available attributes and methods of an object. |
| 1 | `1-my_list.py` | Class `MyList` inherits from `list` with a public method `print_sorted()`. |
| 2 | `2-is_same_class.py` | Function `is_same_class(obj, a_class)` checks if `obj` is **exactly** an instance of `a_class`. |
| 3 | `3-is_kind_of_class.py` | Function `is_kind_of_class(obj, a_class)` checks if `obj` is an instance or subclass of `a_class`. |
| 4 | `4-inherits_from.py` | Function `inherits_from(obj, a_class)` returns True if `obj` is an instance of a subclass of `a_class`. |
| 5 | `5-base_geometry.py` | Empty class `BaseGeometry`. |
| 6 | `6-base_geometry.py` | `BaseGeometry` with method `area()` that raises an Exception: `"area() is not implemented"`. |
| 7 | `7-base_geometry.py` | `BaseGeometry` with `integer_validator(name, value)` to validate integers > 0. |
| 8 | `8-rectangle.py` | `Rectangle` inherits `BaseGeometry` with private width & height; validates using `integer_validator`. |
| 9 | `9-rectangle.py` | `Rectangle` class with implemented `area()` and `__str__()` method `[Rectangle] width/height`. |
| 10 | `10-square.py` | `Square` inherits `Rectangle` with private `size`, implements `area()`. |
| 11 | `11-square.py` | `Square` class with proper `__str__()` returning `[Square] size/size`. |

---

## Examples

### Task 0 – `lookup()`

```python
>>> from 0-lookup import lookup
>>> class MyClass: pass
>>> lookup(MyClass)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
