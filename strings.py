language = 'Python'

print(len(language))

# Acess each indivual letter

letter = language[0]
letters = language[0:3]
letters1 = language[1:]
letters2 = language[:4]
letter3 = language[-1]

print(letter)
print(letters)
print(letters1)
print(letters2)
print(letter3)


street = 'Street Of The DEAD WHITE WALKERS RIP 1 EPISODE'

# String Methods

upper_text = street.upper()
print(upper_text)

lower_text = street.lower()
print(lower_text)

pos_word = street.find('DEAD')
print(pos_word)

pos_word1 = street.find('dead')
print(pos_word1)

rep_word = street.replace('WHITE', "BLACK")
print(rep_word)
