def tellFortune(numberofchildren, partnername, location, jobtitle):
    return "You will be a {jobtitle} in {location}, and married to {partnername} with {numberofchildren} kids.".format(jobtitle = jobtitle, location = location, partnername = partnername, numberofchildren = numberofchildren)
Laurence = tellFortune(2, "Edward", "Fairfield", "programmer")
print(Laurence)
Edward = tellFortune(2, "Laurence", "Cabramatta", "scammer")
print(Edward)
