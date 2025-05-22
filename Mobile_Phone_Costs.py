pictures= int(input("How many pictures do you use in one month?"))
texts= int(input("How many texts do you use in one month?"))
data= int(input("How many data do you use in one month?"))
month= 0.35*pictures+0.10*texts+0.05*data
print("you total bill for your phone is ${:.2f}.".format(month))
if month== 10:
    print("you are better off with a contract")
else:
    print("you are doing fine")
