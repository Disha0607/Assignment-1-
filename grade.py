#Getting the input from the user about the grades
grades = float(input("ENTER YOUR GRADES="))

#function declaration
def calculate(gradesscore):
    if 0 <= gradesscore < 60:
        return "F"
    elif 60 <= gradesscore < 70:
        return "D"
    elif 70 <= gradesscore < 80:
        return "C"
    elif 80 <= gradesscore < 90:
        return "B"
    elif 90 <= gradesscore <= 100:
        return "A"
    else:
        #returing the value
        return "None"

#calling a function
finalgrades = calculate(grades)

print("YOUR GRADES WILL BE=", finalgrades)
