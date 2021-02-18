'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus', 'tunaFISH')

#fish_list = [fish for fish in fish_tuple if 'fish' in fish]
#print(fish_list)

fish_list = [fish for fish in fish_tuple if fish[-4:].lower() == 'fish']
print(fish_list)