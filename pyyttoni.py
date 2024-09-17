# Lisää oma kommentti ja nimikirjaimet alle

import time
import random

# using random.choices() generating random strings
while True:

    res = ''.join(random.choices(string.ascii_letters,k=7))
    f = open(res, "x") 
    print("Hello World!")
    time.sleep(1)
