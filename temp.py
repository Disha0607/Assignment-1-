# temp.py
fahrenheit_temp = input("Enter temperature in Fahrenheit: ")
fahrenheit_temp = float(fahrenheit_temp)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius_temp = convert_to_celsius(fahrenheit_temp)
print("Temperature in Celsius:", celsius_temp)


