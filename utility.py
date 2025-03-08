import random
from string import ascii_lowercase, ascii_uppercase, digits

def get_random_string_for_url(length=7):
    op = ""
    random_chars = list(ascii_uppercase + ascii_lowercase + digits)
    random.shuffle(random_chars)
    for _ in range(length):
        op += random.choice(random_chars)

    return op 
