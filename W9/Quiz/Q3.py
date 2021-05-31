with open('names.txt', 'w') as names:
    name_list = f'lucas\nsimon\njoel\nmarcus\nkarim\ncallum'
    names.write(name_list)

with open('names.txt') as infile, open('formatted-names.txt', 'w') as outfile:
    names = infile.readlines()
    for formatted_names in names:
        outfile.write(formatted_names)
        print(formatted_names.title().strip())