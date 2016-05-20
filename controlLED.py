#LED Control App v1.0
#mbrainar@cisco.com
#

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

print("LED Control App\n")

def menu():
    print('1. Turn LED on\n2. Turn LED off\n3. Exit Application')
    menu_select = input('Enter Selection: ')
    return(str(menu_select))

#print the menu and ask for selection
switch = menu()

while switch != "3":
    if switch == "1":
        print("Turning LED on.")
        GPIO.output(7,True)
        switch = menu()
    elif switch == "2":
        print("Turning LED off.")
        GPIO.output(7,False)
        switch = menu()
    elif switch == "3":
        print("Quitting application.")
        quit()
    else:
        switch = menu()
