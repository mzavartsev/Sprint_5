import random


def gen_email():
    random_numbers = random.randint(000, 999)
    email = f"maksimzavartsev14{random_numbers}@ya.ru"
    return email

def gen_pass():
    sp = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
    passw = ""
    for k in range(3):
        r = "".join(random.choices(sp, k=3))
        random_pass = str(random.randint(000,999))
        passw += r + random_pass
    return passw
