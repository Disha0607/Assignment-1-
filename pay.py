def unfair_weekly_paycheck_amount(hours_worked):
    return int(hours_worked) * 15

def fair_weekly_paycheck_amount(hours_worked):
    return hours_worked * 15

# Example input
hours_worked = float(input("Enter hours worked this week: "))

unfair_pay = unfair_weekly_paycheck_amount(hours_worked)
fair_pay = fair_weekly_paycheck_amount(hours_worked)

print("Unfair paycheck amount:", unfair_pay)
print("Fair paycheck amount:", fair_pay)
