# code from favorite_languages.py in book
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
poll_list = ['mckinsey', 'jen', 'phil', 'newton', 'monica']

for name in poll_list:
#    print(f'Hi {name.title()}')
    if name in favorite_languages:
        print(f'Thank you for taking our poll {name.title()}!')
    
    else:
        print(f'Please take our poll {name.title()}.')

    
  
