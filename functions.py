# def greeting():
# print('Hello there my friend')
# print('what is your name')
# name = input()
# print('Nice to meet you ' + name)


def greeting(name):
    print('Hello there ' + name)


print('The function is not running yet')

# greeting()
# greeting()

greeting('Salah')


''' def multiply_by_10(number):
    print(10 * number)


multiply_by_10(50) '''


def multiply_by_10(number):
    return 10 * number


multipled_number = multiply_by_10(50)

print(multipled_number)


def add(number, by=1):
    return number + by


added_number = add(10, 5)
added_number1 = add(10)
added_number2 = add(number=10, by=5)
print(added_number, added_number1, added_number2)
