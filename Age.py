name=input("Enter your name")
age=int(input("Enter your age in years"))
days_in_a_year=365
hours_in_a_day=24
minutes_in_a_hour=60
seconds_in_a_minute=60

daysAlive = age * days_in_a_year
hoursAlive = daysAlive * hours_in_a_day
minutesAlive = hoursAlive * minutes_in_a_hour
secondsAlive = minutesAlive * seconds_in_a_minute

print("Hi", name + "!")
print(f"You have been alive for approximately:")
print(f"{daysAlive} days")
print(f"{hoursAlive} hours")
print(f"{minutesAlive} minutes")
print(f"{secondsAlive} seconds")
             