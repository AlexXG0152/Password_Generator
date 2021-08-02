import random

"""
I've seen the task of implementing a password generator as a practice for developers. 
Here is my implementation of this task.
1. I deliberately removed the following characters 0, 1, I, O, o. 
Due to the fact that in some fonts they are very similar to each other and this can cause difficulties for the user.
2. Also, I implemented a simple check that the user should enter a positive number of the desired password length,
and not a text, letter, negative number, float number.
3. Also, verification is built into password generation function. Thus, it can be used in a loop.
"""

symbols = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ!#$%&"


def ask_user():
    """
    We ask user how long password he needs and check his input.
    """
    password_lenght = 0
    while password_lenght == 0:
        try:
            password_lenght = int(input("How long password you want? Enter the number of digits... "))
            if password_lenght <= 0:
                print("Try to enter any number greater than 0...")
                continue
            return password_lenght
        except Exception:
            continue

    
def password_generator(password_lenght):
    """
    Checking input data and generating password of a given length.
    """
    try:
        password = [random.choice(symbols) for i in range(password_lenght) if password_lenght >=1]
        print(f"Your password is:  {''.join(password)} \nTnank you!")
        return password
    except Exception:
        pass


if __name__ == "__main__":
    password_generator(ask_user())
