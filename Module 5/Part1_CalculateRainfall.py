# Module 5: Critical Thinking Assignment, Part 1:

# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years. The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.


print("Welcome to Rainfall calculator\n\n")

rainfall_amounts = []
month_names = [{"number": 1, "name": "January"}, {"number": 2, "name": "February"},
               {"number": 3, "name": "March"}, {"number": 4, "name": "April"},
               {"number": 5, "name": "May"}, {"number": 6, "name": "June"},
               {"number": 7, "name": "July"}, {"number": 8, "name": "August"},
               {"number": 9, "name": "September"}, {"number": 10, "name": "October"},
               {"number": 11, "name": "November"}, {"number": 12, "name": "December"}
               ]
years = int(input("Number of years to calculate?"))

def get_month_name(month_in):
    __month = None
    for month_name in month_names:
        if month_name["number"] == month_in:
            __month = month_name["name"]
            break
    return __month

total_inches = 0
for year in range(0, years):
    print("Year " + str(year + 1) + ": \n")
    for month in range(1, 13):
        name = get_month_name(month)
        rainfall = float(input("inches of rainfall for {name}? ".format(name=name)))
        total_inches += rainfall
        rainfall_amounts.append({"year": year, "month": name, "amount": rainfall})

print("\nAnalysis: ")

month_count = rainfall_amounts.__len__()
print("Number of months: {month_count}".format(month_count=month_count))
print("Total inches of rainfall: {inches:.2f}".format(inches=total_inches))
print("Average rainfall per month for the entire period: {avg_inch_per_month:.2f}".format(
    avg_inch_per_month=(total_inches / month_count)))

