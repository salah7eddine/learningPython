users = ['Mizo', 'Mery', 'Papi', 'Gone', 'Killua', 'S7E']

print(users)
print(users[1])
print(users[1:4])

alot_zeros = [0] * 20

print(alot_zeros)

# Unpacking
items = ['Laptop', 'Phone', 'Joystick']
# laptop, phone, Joystcik = items 
laptop, *other = items 

laptop = items[0]
print(laptop)
print(other)

# Add Items

users.append('New Item')
users.insert(0, 'begging item')

print(users)
# Remove Item

users.pop()
print(users)

# Tupple
# letters = ('a', 'b', 'c', 'd')
# Sets
letters = {'a', 'b', 'c', 'd'}

