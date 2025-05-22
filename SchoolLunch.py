schoolMoney= float(input("How much money you had for your school lunch today?"))
endMoney= float(input("How much money you spent on your school lunch today?"))
remainingMoney= schoolMoney-endMoney
print("You have ${:.2f} left.".format(remainingMoney))
