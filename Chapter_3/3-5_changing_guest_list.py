# i can't believe i wrote this in the REPL previously. Can't get that back so here we go
guest_list = ['Ann', 'Hafsa', 'Kam', 'Clara']
for guest in guest_list:
    print(f'Hi {guest}, you are invited to my dinner party at 1122 Parkinson Drive. See you then!')
    
print(f"Looks like {guest_list[1]} can't make it to the party.")

guest_list[1] = 'Soon-ja'

for guest in guest_list:
    print(f'Hi {guest}, you are invited to my dinner party on January 5 at 6pm. See you then!')
