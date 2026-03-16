from pathlib import Path

path = Path('txt_files/the_new_hackers_dictionary.txt')
contents = path.read_text()

# count the number of times the words - 'hackers' and 'the ' appears in the text file
count_hacker = contents.lower().strip().count('hacker')
count_the = contents.lower().strip().count('the ')

print(count_hacker)
print(count_the)

