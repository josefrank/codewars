"""
Consider an array/list of sheep where some sheep may be missing from
their place. We need a function that counts the number of sheep present
in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

The correct answer would be 18.

Hint: Don't forget to check for bad values like null/undefined
"""

# Solution

def count_sheeps(sheep):
    # Simplest form of counter using a for loop and a list.
    counter = 0
    for s in sheep:
        if s == True:
            counter += 1
    return counter

# Test

some_sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True, True]

result = count_sheeps(some_sheeps)

print(result)
