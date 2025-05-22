SecretPassword="Hi"
enterSecret=input("Enter the secret password")
if SecretPassword==enterSecret:
    print("Access granted")
    
    happy=int(input("On a scale 1-10, how happy are you?"))
    if happy <= 3:
        print("Cheer up, you only have 1-400 trillion chance to be alive")
    elif happy <= 4 <= 7:
        print("I am happy you are not doing bad")
    elif happy >= 8:
        print("I am really happy that you are doing amazing")
    else:
        print("Please enter a number between 1-10")
else:
    print("You got the incorrect password, please try again")