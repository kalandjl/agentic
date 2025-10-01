import random

def generate_hex_id(): 

    hex_chars = "0123456789abcdef"
    return ''.join(random.choice(hex_chars) for _ in range(20))


