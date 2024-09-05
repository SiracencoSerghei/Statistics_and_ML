#!/usr/bin/env python
# coding: utf-8

# What are (is?) data?
# Code: Representing types of data on computers

# Create variables of different types (classes)

# data numerical (here as a list)
numdata = [1, 7, 17, 1717]

# character / string
chardata = 'xyz'

# double-quotes also fine
strdata = "x"

# boolean (aka logical)
logitdata = True  # notice capitalization!

# a list can be used like a MATLAB cell
listdata = [[3, 4, 34], 'hello', 4]

# dict (kind of similar to MATLAB structure)
dictdata = {
    'name': 'Mike',
    'age': 25,
    'occupation': 'Nerdoscientist'
}

# Inspect the variables (this will print them)
print("Numerical data:", numdata)
print("Character data:", chardata)
print("String data:", strdata)
print("Boolean data:", logitdata)
print("List data:", listdata)
print("Dictionary data:", dictdata)


# Clear the Python workspace (not usually recommended to do this in a script)
# To clear variables in a script, you can manually delete them
del numdata, chardata, strdata, logitdata, listdata, dictdata

# Check if variables are cleared (this will raise a NameError if they are cleared)
try:
    print(numdata)
except NameError:
    print("Variables have been cleared.")


