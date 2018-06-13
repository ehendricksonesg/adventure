# This file is for external, custom functions
# Enjoy

import random


def rand_num(your_number):
    randy = random.randint(1, int(3 * your_number))

    if int(randy) >= int(2 * your_number):
        randy = random.randint(1, int(2 * your_number))
    if int(randy) >= int(your_number):
        randy = random.randint(1, int(your_number))

    return randy
