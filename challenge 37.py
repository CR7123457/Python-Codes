countryPop = { "Japan":"127000000",
               "Germany":"81000000",
               "Iran":"77000000",
               "UK":"64000000",
               "Canada":"33000000",
               "Australia":"23000000",
               "USA":"317000000",
               "Bulgaria":"7000000",
               "Sweden":"10000000"}
print("Choose from the available countries:", ", ".join(countryPop.keys()))
population=input("Choose a country")
population1=input("choose another country")
if population in countryPop and population1 in countryPop:
    user1= int(countryPop[population])
    user2= int(countryPop[population1])
    populationTotal= user1 + user2
    print(f"The population of the two countries you chose is {populationTotal:,}")
else:
    print("You have not chose a country from the list")




