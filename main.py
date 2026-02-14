#Title: Average Rainfall
#Author: Dominic Corneliusen
#Date last modified: 2/13/2026

#Variables
numberOfYears = int(input("How many years are you collecting data from?"))
count = numberOfYears
monthsOfTheYear = ['January','February','March','April','May','June',
                   'July','August','September','October','November','December']
totalRainfall = 0

#While Loop
while count > 0:
    for month in monthsOfTheYear:
        printText = 'Enter the amount of rainfall in inches from', month, '.'
        rainfallInMonth = int(input(printText))
        totalRainfall = totalRainfall + rainfallInMonth
    count -= 1
#Closing statements
amountOfMonths = 12 * numberOfYears
averageRainfall = totalRainfall / amountOfMonths
print("There was", amountOfMonths, "months of data reported.")
print("The total amount of rainfall is", totalRainfall, "inches.")
print("The average rainfall is", averageRainfall, "inches.")