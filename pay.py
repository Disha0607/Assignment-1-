def fair_weekly_paycheck_amount(hours):
    return hours * 30

def unfair_weekly_paycheck_amount(hours):
    rounded_hours = int(hours)
    return rounded_hours * 15

if __name__ == "__main__":
    # Sample usage
    hrs = float(input("Enter number of hours worked: "))
    print("Fair weekly paycheck amount:", fair_weekly_paycheck_amount(hrs))
    print("Unfair weekly paycheck amount:", unfair_weekly_paycheck_amount(hrs))
