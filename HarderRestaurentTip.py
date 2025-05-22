#Asking the user for information
totalTip= float(input("How much did your meal cost?" ))
tipPercentage=float(input("What percentage of tip would you like to give in 2 decimal places? eg: 15%= 1.15" ))
totalPeople=int(input("How many people do you want to split the bill with?"))
taxi=float(input("What is the distance of the taxi in Miles?"))
#Making calculations
tip= totalTip*tipPercentage
taxiCost= taxi*0.45
tipEachPerson= totalTip/tipPercentage
#Print the information
print("Your total meal cost is ${:.2f}.".format(tip))
print("Each person has to pay ${:.2f}.".format(tipEachPerson))
print("Your total cost for the taxi is ${:.2f}.".format(taxiCost))



