#either male or female
choice = input("What is your gender (M/F):")
choice = choice.upper()
if choice =="M":
    print("Congratulation! You get 10% discount off grooming products today, for sale in superdrug the chemist")
elif choice =="F":
    print("Congratulation! You get a free manicure today, for sale in superdrug the chemist")
else:
    print("Invalid gender input, please enter F or M")
