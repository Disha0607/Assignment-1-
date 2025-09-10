#Getting the input from the user about the grades
grades = float(input("ENTER YOUR GRADES="))

#function declaration
def calculate(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    elif 0 <= grade < 60:
        return "F"
    else:
        return None


#calling a function
finalgrades = calculate(grades)

print("YOUR GRADES WILL BE=", finalgrades)

