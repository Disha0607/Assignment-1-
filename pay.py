# pay.py

def compute_pay(hours, rate):
    return hours * rate

# Optional: input/output only runs if the script is called directly, not on import
if __name__ == "__main__":
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    print(compute_pay(hours, rate))
