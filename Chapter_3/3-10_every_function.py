# practicing every subtopic in chapter 3

# creating lists
mountains = ['sierra nevada', 'everest', 'balkan', 'dolomite']
rivers = ['yellow river', 'nile', 'amazon', 'mississipi']
countries = ['canada', 'kenya', 'netherlands', 'germany', 'tanzania']
cities = ['berlin', 'san francisco', 'new york', 'vienna']
languages = ['german', 'spanish', 'farsi', 'yoruba']

# accessing elements in lists using index postions
print(mountains[0])
print(cities[3])
print(languages[-1])

# using individual items from lists
question = f'How is {languages[0]} learning going?'
print(question)
print(f'If only I could read {languages[-1]} a bit better.')

# modifying, adding and removing elements

#replacing
mountains[1] = 'alpine'
print(mountains)

#adding
countries.append('south africa')
print(countries)

#inserting
cities.insert(2, 'nairobi')
print(cities)

#removing 
del countries[-2]
print(countries)

removed_river = rivers.pop()
print(removed_river)
print(rivers)

rivers.remove('yellow river')
print(rivers)

# sorting with sort(permanent)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)

#sorting with sorted(temporary)
print(sorted(countries))
print(countries)

#reverse list(permanent, reverse by reversing(😂))
countries.reverse()
print(countries)
countries.reverse()
print(countries)

# length of lists
print(len(mountains))
print(len(rivers))
print(len(countries))
print(len(cities))
print(len(languages))

# index error
rivers[3]
languages[5]