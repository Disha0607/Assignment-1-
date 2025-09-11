def calculate(grade):
    if grade == -1:
        return "N/A"
    elif grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    try:
        g = float(input())
        print(calculate(g))
    except Exception:
        print("N/A")
