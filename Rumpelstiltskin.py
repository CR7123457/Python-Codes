myName = "Keshav"

while True:
    # Ask the user for their first name
    userName = input("Please enter your first name: ")
    
    # Check if the name matches your name
    if userName == myName:
        print(f"Welcome,{myName}, nice to meet you!")
        break  # Exit the loop
    else:
        print("Sorry thats not my name, please try again")