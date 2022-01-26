#Генератор паролей v2
import os
import random 
import secrets
import string
import time

def generator_random_string(lenght):
    letters_and_digits = string.ascii_letters + string.digits
    crypta_rand_string = '' .join(secrets.choice(letters_and_digits) for i in range(lenght))
    print("Crypto password of", lenght, "symbols it:", crypta_rand_string)

print("Program creator: Rubilom")
time.sleep(1)
print("To stop the password generation cycle, press CTRL + C")
try:
    while True:
        print("How many characters will the password be?: ")
        print(generator_random_string(int(input())))
except KeyboardInterrupt:
    pass
    


