import random


class Generator:

    def __init__(self):
        # list comprehension to get list of single letter or sign or number
        self.letters = [i for i in "0123456789!@#$%^&*-_+=,<.>/?;:`~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]

    def generate_password(self, number):
        # function to get the list of random letters and return it
        password = []
        for n in range(number):
            password.append(random.choice(self.letters))
        return password