def add_two_numbers(a, b):
    return a + b


def multiply_two_numbers(a, b, ):
    return a * b


# print(add_two_numbers(1, 2))
# print("l")

character_name = "John"
character_age = 35
is_male = True

print("There once was a man named " + character_name)
print("He was " + str(character_age))

if is_male:
    print("He is a man")

print("Giraffe\n\"Academy\"")
phrase = "Phrase"
print(phrase)
print(str(add_two_numbers(5, 6) // multiply_two_numbers(1, 3)))
print(phrase + " c'est cool.")
print(phrase.lower())
print(phrase.islower())

# name = input("Enter your name: ")
# age = input("How old are you: ")
# print("Hello " + name + " You are " + age)

# Lists
lucky_numbers = [149, 22, 482, 29, 247]
random_list = ["master", "coal", "ceremony", "moon", "besides"]
random_list.extend(lucky_numbers)
print(random_list)
print(type(random_list[2]))

# for i in range(len(random_list)):
#     print(type(random_list[i]))


# Tuple
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0])


# Functions and return statement
def say_hi(name, age):
    print("Hello " + name + " you are: " + str(age))


say_hi("Lukas", 17)


# words = ["loaf", "excuse", "staff", "moreover", "buy"]
#
# for elem in words:
#     say_hi(elem)

def cube(num):
    return num ** 3


result = cube(4)
print(result)

# If statements
is_male_if = True
is_tall = True

if is_male_if:
    print("You are a male")
else:
    print("You are not a male")


# If statements and comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


assert max_num(4, 6, 3) == 6
assert max_num(199, 491, 592) == 592
assert max_num(0, 0, 0) == 0
