'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

full_name = []
surname = []
first_name = []
quotes = []
# iterate through the list and get dictionaries
for dict_ in famous_quotes:
    full_name.append(dict_["full_name"])
    quotes.append(dict_["quote"])

# iterate through the dictionary so that we can break up the names into first and last name
for name in full_name:
    split_name = name.split(" ")
    last_name = split_name[-1]
    surname.append(last_name)
    f_name = split_name[0]
    first_name.append(f_name)

print(surname, first_name)

# think of zip like a column/row matrix
for final_line in zip(quotes, surname, first_name):
    print(f"{final_line[0]} - {final_line[1]}, {final_line[2]}")








