def unfair_weekly_paycheck_amount(hours):
    return hours * 7.5

def fair_weekly_paycheck_amount(hours):
    if hours <= 40:
        return hours * 7.5
    else:
        overtime = hours - 40
        return (40 * 7.5) + (overtime * 11.25)
