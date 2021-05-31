with open('names.txt', 'w') as names:
    name = input('Enter a name: ')
    while name != '':
        names.write(name.title() + '\n')
        name = input('Enter a name: ')

with open('names.txt', 'r') as names:
    lines = names.read()
    print(lines.strip())