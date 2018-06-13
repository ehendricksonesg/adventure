# import random
from practice_module import rand_num

print("Hello")
print("Today we are going to do some dice rolls")
print("With a min of 1, what would you like the max value to be?")

your_number = input("Max value: ")

print("Are you sure that you want a max of " + your_number + "?")
answer = input("y/n: ")

if answer == "n":
    your_number = input("Max value: ")

print("Okay. Lets roll!")

rand = rand_num(your_number)

print("You rolled a " + str(rand) + "!")

