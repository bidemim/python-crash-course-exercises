guest_list = ['Ann', 'Soon-ja', 'Kam', 'Clara']

for guest in guest_list:
    print(f'Hello {guest}, I found a bigger table!')

guest_list.insert(0, 'Doreen')
guest_list.insert(2, 'Eric')
guest_list.append('Bukky')

for guest in guest_list:
    print(f'Hi {guest}, you are invited to my dinner party on January 5 at 6pm. See you then!\n')
    print(f'Hi {guest}, unfortunately my new table would not arrive before January 5, I now only have space for two guests.')

uninvite_guest = guest_list.pop()
print(f"Hello {uninvite_guest}, I'm sorry I have to cancel our dinner plans.")
uninvite_guest = guest_list.pop()
print(f"Hello {uninvite_guest}, I'm sorry I have to cancel our dinner plans.")
uninvite_guest = guest_list.pop()
print(f"Hello {uninvite_guest}, I'm sorry I have to cancel our dinner plans.")
uninvite_guest = guest_list.pop()
print(f"Hello {uninvite_guest}, I'm sorry I have to cancel our dinner plans.")
uninvite_guest = guest_list.pop()
print(f"Hello {uninvite_guest}, I'm sorry I have to cancel our dinner plans.")

for guest in guest_list:
    print(f'Hi {guest}, you are still invited, please let me know your plans.\n')
del guest_list[0:]
print(guest_list)
