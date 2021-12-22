def calculateSupply(currentage, maximumage, amount_per_day):
    amount = round((maximumage - currentage)*amount_per_day)
    return ("You will need {amount_per_day} to last you until the ripe old age of {maximumage}".format(amount_per_day = amount, maximumage = maximumage))
firstsupply = calculateSupply(10, 50, 20.31)
print(firstsupply)


