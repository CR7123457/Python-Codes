number= int(input("What number do you want to see in time tables?"))
print(number, "Times table\n")
for j in range(1, 13):
     print (number, "times", j, " = ", number*j)
