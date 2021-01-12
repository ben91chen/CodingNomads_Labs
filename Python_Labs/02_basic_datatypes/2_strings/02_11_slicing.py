
'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

# get a name from user
name = input("What's your name? ")
first_letter = name[0]
stripped_name = name.strip(first_letter)

pig_latin_name = stripped_name + first_letter + "ay"
print(pig_latin_name)
