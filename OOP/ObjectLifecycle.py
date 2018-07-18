# Object lifecycle test program for Python

# The lifecycle of an object is made up of its creation, manipulation, and destruction.
# Definition > instantiation (__init__) > memory allocated to store the instance > __new__

# Destruction occurs when its reference count reaches zero.
# Del statement reduces reference count by 1
# __del__

# Example:
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42>
c = [a]  # Increase ref. count  of <42>

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42>
c[0] = -1  # Decrease ref. count  of <42>
