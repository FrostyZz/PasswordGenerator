import random
import pyfiglet
'''
___________                      __          
\_   _____/______  ____  _______/  |_ ___.__.
 |    __) \_  __ \/  _ \/  ___/\   __<   |  |
 |   \     |  | \(  <_> )___ \  |  |  \___  |
 \___/    |__|   \____/____  > |__|  / ____|
  \/                       \/        \/     
'''

num = int(input("How long do you want your password to be? \n"))

def PasswordGenerator(num):
    ayy = random.randrange(0,3)
    password = ""
    for ayy in range(0,num):
        babyy = random.randrange(0,3)
        if babyy == 0:
            babyy = random.randrange(65,91)
            password+=chr(babyy)
        elif babyy == 1:
            babyy = random.randrange(97,123)
            password+=chr(babyy)
        else: 
            babyy = random.randrange(48,58)
            password+=chr(babyy)
    return password

PasswordGenerator(num)
print(PasswordGenerator(num))
from pyfiglet import Figlet
custom_fig = Figlet(font='graffiti')
print()
print()
print()
print()
print("Written By:")
print(custom_fig.renderText('Frosty'))
input('Press ENTER to exit')
