'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
a = 0
e = 0
i = 0
o = 0
u = 0

user_string = input("Type a sentence or phrase: ")

for vowel in user_string:
    if vowel == 'a':
        a += 1
    elif vowel == "e":
        e += 1
    elif vowel == "i":
        i += 1
    elif vowel == "o":
        o += 1
    elif vowel == "u":
        u += 1


print(f"""Breakdown of vowels in your sentence:
a: {a}
e: {e}
i: {i}
o: {o}
u: {u}
""")


