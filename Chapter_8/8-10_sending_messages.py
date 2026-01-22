def show_messages(messages):
    print(f'\nShowing message:')
    for message in messages:
        print(message)
       

def send_messages(messages):
    while messages:
        display_message = messages.pop()
        print(f'Moving message: {display_message}\n')
        sent_messages.append(display_message)

messages = [
    'Good things take time.',
    'A stitch in time saves nine.',
    'Make good friends.',
            ]
sent_messages = []

send_messages(messages)

print(messages)
print(sent_messages)