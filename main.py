#Title: Bank Balance
#Author: Dominic Corneliusen
#Date last modified: 2/13/2026

#Variables
userBudgetForMonth = int(input("How much money have you budgeted for this month?$"))
expenseCategories = ['Housing','Transportation','Food','Utilities','Insurance',
                     'Personal Care','Entertainment','Family care','Miscellaneous']
totalAmount = 0
#For loop
for expense in expenseCategories:
    text = 'How much did you spend in the', expense, 'category this month?$'
    categoryAmount = int(input(text))
    totalAmount = totalAmount + categoryAmount
#Closing Statements
print('Your budget for the month is $', userBudgetForMonth, '. You spent $', totalAmount, '.')
if totalAmount > userBudgetForMonth:
    print('Since your spending was greater than your budget, '
          'you are over your spending budget.')
else:
    print('Since your spending was less than your budget, you are under '
          'your spending budget. Congratulations!')