import string
import random

password_length = 10            #we can also take the length from user as input

def password_generator(length):
    password_characters = string.ascii_letters + string.digits + string.ascii_letters + string.punctuation
    new_password = "".join(random.choice(password_characters) for i in range(password_length))
    print(f"Your new password is {new_password}")

password_generator(password_length)
