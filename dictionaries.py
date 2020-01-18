user = {
  "name": "Mizo",
  "email": "mizo@gmail.com",
  "age": 25,
  "purchases": [1, 2, 3, 4]
}

# print(user['name'])
# print(user['email'])

# user['name'] = 'Mery'
# user['email'] = 'meryem@gmail.com'

# print(user)

# for item in user:
#   print(item)

# for key in user:
#   print(key)

# print(user.keys())
# print(user.items())

# for key, val in user.items():
#   print(key)
#   print(val)

if 'logged' in user:
  print('it is!')

del user['purchases']

print(user)