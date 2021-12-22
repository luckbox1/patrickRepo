def assigngrade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "F"
print(assigngrade(80))