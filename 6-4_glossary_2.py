# already had the for loop working in the previous exercise
glossary = {
    'string literal': 'A series of characters surrounded by quotes.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'conditional statement': 'A block of code that runs only if a certain condit\
ion is true.',
    'truthy value': 'A value that evaluates to True in a boolean context.',
    'f-string': 'A string that is prefixed with f and allows embedding expressio\
ns inside curly braces.',
}
print("Glossary Terms:\n")
for index, (term, definition) in enumerate(glossary.items(), start=1):
    print(f'{index}. {term.title()}: {definition}\n')
