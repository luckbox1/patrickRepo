
#creating the function to input the integer
def testnumber(number):

#divisiliby by all 3 factors
        if number % 105 == 0:
            return "PlingPlangPlong"

#divisibility by 2 factors
        elif number % 35 == 0:
            return "PlangPlong" 
        elif number % 21 == 0:
            return "PlingPlong"
        elif number % 15 == 0:
            return "PlingPlang"

#divisibility by 1 factor
        elif number % 7 == 0:
            return "Plong"
        elif number % 5 == 0:
            return "Plang"
        elif number % 3 == 0:
            return "Pling"

#not divisible
        else:
           return number 

print(testnumber(223))

