"""
Problem 9-13 of Python Crash Course
"""

from collections import OrderedDict
definitions = OrderedDict()
definitions['variable'] = 'Holds the value associated with it.'
definitions['string'] = 'A series of characters.'
definitions['concatenation'] = 'Combining 2 strings together with + symbol.'
definitions['float'] = 'In Python, any number with a decimal point.'


for term, definition in definitions.items():
    print(term.title() + ":\n\t" +
          definition + "\n")
