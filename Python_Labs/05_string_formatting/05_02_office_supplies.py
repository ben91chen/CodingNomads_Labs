'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

full_name = []
first_name = []
last_name = []
office_supply = []



# iterate over list and get dictionaries, then append them to list
for dict_ in office:
    full_name.append(dict_["full_name"])
    office_supply.append(dict_["item"])

# separate first name from last name
for name in full_name:
    split_name = name.split(" ")
    first_name.append(split_name[0])
    last_name.append(split_name[1])

# put the f-string together

for sentence in zip(first_name, last_name, office_supply):
    length = (len(f"{sentence[1]}, {sentence[0]}"))
    print(f'{sentence[1]}, {sentence[0]}{sentence[2].rjust(50 - length)}')

# how do I get the last office_supply to ljust in the same position on the right hand side?
