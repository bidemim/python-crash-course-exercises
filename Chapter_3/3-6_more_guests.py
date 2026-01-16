guest_list = ['Ann', 'Soon-ja', 'Kam', 'Clara']

for guest in guest_list:
    print(f'Hello {guest}, I found a bigger table!')

guest_list.insert(0, 'Doreen')
guest_list.insert(2, 'Eric')
guest_list.append('Bukky')

for guest in guest_list:
    print(f'Hi {guest}, you are invited to my dinner party on January 5 at 6pm. See you then!')