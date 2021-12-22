def calculateDogAge(puppyage, rate):
    return ("Your doggie is {humanage} years old in dog years!").format(humanage = puppyage*rate)
firstage = calculateDogAge(10, 3)
print(firstage)
