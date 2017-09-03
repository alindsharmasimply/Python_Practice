cost = input("Enter cost of the meal")
tax = (cost*18.0)/100
tip = ((cost-tax)*18.0)/100
print "Total cost of the meal is" , cost + tax + tip
print "tip =" , tip
print "tax =" , tax