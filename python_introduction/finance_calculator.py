monIncome = input("Enter your monthly income: ")
monExpenses = input("Enter your total monthly expenses: ")

monIncome = int(monIncome)
monExpenses = int(monExpenses)

interest = .05  # Example interest rate of 5%
monSavings = monIncome - monExpenses

projectedSavings = int(monSavings * 12 + (monSavings * interest * 12))
print(f"Your monthly savings are: ${monSavings}.")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}.")