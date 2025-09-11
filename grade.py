def calculate(grade):
    if grade < 0 or grade > 100:
        return "N/A"
    elif grade < 60:
        return "F"
    elif grade < 70:
        return "D"
    elif grade < 80:
        return "C"
    elif grade < 90:
        return "B"
    else:
        return "A"
