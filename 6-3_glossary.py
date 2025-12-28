glossary = {
    'string literal': 'A series of characters surrounded by quotes.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'conditional statement': 'A block of code that runs only if a certain condition is true.',
    'truthy value': 'A value that evaluates to True in a boolean context.',
    'f-string': 'A string that is prefixed with f and allows embedding expressions inside curly braces.',
    'boolean': 'A data type that can be either True or False.',
    'loop': 'A sequence of instructions that repeats until a certain condition is met.',
    'function': 'A block of reusable code that performs a specific task.',
    'variable': 'A named location used to store data in memory.',
    'tuple': 'An immutable ordered collection of items.',
    'set': 'An unordered collection of unique items.',
    'immutable': 'A property of an object that prevents it from being changed after it is created.',
    'mutable': 'A property of an object that allows it to be changed after it is created.',

}

print("Glossary Terms:\n")
for index, (term, definition) in enumerate(glossary.items(), start=1):
    print(f'{index}. {term.title()}: {definition}\n')
