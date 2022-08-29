import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = "(){}[],;:.-_?/|\\?+!@#$%^&*= <>~`"

upper, lower, nums , syms = True, True, True, False

all = ""

if upper:
    all += uppercase_letters
    
if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols
    
length = 8
amount = 20

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
