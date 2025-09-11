# GETTING USER INPUT
number_of_hours = float(input("ENTER THE NUMBERS OF HOURS YOU HAVE WORKED = "))

# DEFINING A FUNCTION
def unfair_weekly_paycheck_amount(number_of_hours):
    # rounded hours
    rounded_hours = int(number_of_hours)
    pay = 15 * rounded_hours
    # RETURNING THE PAY
    return pay

# CALLING THE FUNCTION
total_pay = unfair_weekly_paycheck_amount(number_of_hours)
print("THE UNFAIR WEEKLY AMOUNT =", total_pay)

def fair_weekly_paycheck_amount(n_hours):
    payrate = 15 * n_hours
    return payrate

payamount = fair_weekly_paycheck_amount(number_of_hours)
print("THE FAIR WEEKLY AMOUNT =", payamount)
