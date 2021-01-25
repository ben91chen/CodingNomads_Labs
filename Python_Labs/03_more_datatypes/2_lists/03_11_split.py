'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

user_input = input("Type a sentence: ")
split_sentence = user_input.split()

list = []
for word in split_sentence:
    list.append(word)

print(list)


word_counter = {}
for word_ in list:
    if word_ in word_counter:
        word_counter[word_] += 1
    else:
        word_counter[word_] = 1
print(word_counter)

most_common_word = sorted(word_counter, key = word_counter.get, reverse = True )
top_1 = most_common_word[0]
print(top_1)




