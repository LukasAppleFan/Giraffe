def add_two_numbers(a, b):
    return a + b


def multiply_two_numbers(a, b,):
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

lucky_numbers = [149, 22, 482, 29, 247]
random_list = ["master", "coal", "ceremony", "moon", "besides"]
random_list.extend(lucky_numbers)
print(random_list)
print(type(random_list[2]))

# for i in range(len(random_list)):
#     print(type(random_list[i]))
z