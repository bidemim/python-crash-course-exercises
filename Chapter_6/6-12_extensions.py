users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
	    'age': 63,
		'expertise': 'physics',
		
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
	    'age': 44,
		'expertise' : 'chemistry'
	,
        },
    }
for username, user_info in users.items():
	print(f"\nUsername: {username.upper()}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	age = user_info['age']
	expertise = user_info['expertise']
	
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
	print(f"\tAge: {age}")
	print(f"\tDomain Expertise: {expertise.title()}")
	
	