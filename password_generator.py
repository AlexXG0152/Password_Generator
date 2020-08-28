import random

"""
I've seen the task of implementing a password generator as a practice for developers. 
Here is my implementation of this task.
1. I deliberately removed the following characters 0, 1, I, O, o. 
Due to the fact that in some fonts they are very similar to each other and this can cause difficulties for the user.
2. Also, I implemented a simple check that the user should enter a positive number of the desired password length,
and not a text, letter, negative number, float number.
"""

letters = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ!#$%&"


def password_generator():
    password = ""
    password_lenght = input("How long password you want? Enter the number... ")

    try:
        password_lenght = int(password_lenght)
        if password_lenght > 0:
            for _ in range(password_lenght):
                choice = random.choice(letters)
                password += str(choice)
            print(f"Your password is:  {password}")
            print("Thank you!")
        else:
            print("Try to enter any number greater than 0...")
            password_generator()
    except ValueError:
        password_generator()
    return password


password_generator()