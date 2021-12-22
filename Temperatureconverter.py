def celsiusToFahrenheit(Celsius):
    fahrenheit = 1.8*Celsius + 32
    return fahrenheit
usercelsius = float(input("What is your temperature in Celsius? "))
tempinf = celsiusToFahrenheit(usercelsius)
print(str(usercelsius) + "\N{DEGREE SIGN}C is " + str(tempinf) + "\N{DEGREE SIGN}F")
3

