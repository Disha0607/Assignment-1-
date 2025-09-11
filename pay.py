def unfair_weekly_paycheck_amount(number_of_hours):
    rounded_hours = int(number_of_hours)
    pay = 15 * rounded_hours
    return pay

def fair_weekly_paycheck_amount(number_of_hours):
    pay = 15 * number_of_hours
    return pay

# Get user input
number_of_hours = float(input("Enter the number of hours you have worked this week: "))

# Calculate pays
unfair_pay = unfair_weekly_paycheck_amount(number_of_hours)
fair_pay = fair_weekly_paycheck_amount(number_of_hours)

# Print results
print("The unfair weekly paycheck amount is:", unfair_pay)
print("The fair weekly paycheck amount is:", fair_pay)
