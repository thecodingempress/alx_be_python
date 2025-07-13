monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_income = int(monthly_income)
monthly_expenses = int(monthly_expenses)

interest = .05  # Yearly interest rate of 5%
monthly_savings = monthly_income - monthly_expenses

projected_savings = int(monthly_savings * 12 + (monthly_savings * interest * 12))
print(f"Your monthly savings are: ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")