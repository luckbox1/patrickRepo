def pluralize(noun, number):
    if number == 1:
        return noun
    else:
        return(str(number) + " " + noun + "s")
print(pluralize("cat", 3))
print(pluralize("cat", 1))