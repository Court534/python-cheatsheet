# PyLint a widely used tool that checks for errors in Python code and encourages good Python coding

# example 1

a = 1
b = 2

print(a)
print(B) # Made a mistake here

# when i run pylint pylint.py (The name of the python file) it returns:
# ************* Module pylint
# pylint.py:9:0: C0305: Trailing newlines (trailing-newlines)
# pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# pylint.py:4:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# pylint.py:5:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# pylint.py:8:6: E0602: Undefined variable 'B' (undefined-variable)

# -----------------------------------
# Your code has been rated at 0.00/10

# example 2

A = 1
B = 2

print(A)
print(B)

# ************* Module pylint
# pylint.py:1:0: C0114: Missing module docstring (missing-module-docstring)

# -------------------------------------------------------------------
# Your code has been rated at 7.50/10 (previous run: 0.00/10, +7.50)


# example 3

''' Simple script '''

A = 1
B = 2

print(A)
print(B)

# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 7.50/10, +2.50)
