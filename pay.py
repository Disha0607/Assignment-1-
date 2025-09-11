def fair_weekly_paycheck_amount(hours):
    return hours * 30

def unfair_weekly_paycheck_amount(hours):
    rounded_hours = int(hours)
    return rounded_hours * 15

if __name__ == "__main__":
    hrs = float(input("Enter hours worked: "))
    print("Fair weekly pay:", fair_weekly_paycheck_amount(hrs))
    print("Unfair weekly pay:", unfair_weekly_paycheck_amount(hrs))
