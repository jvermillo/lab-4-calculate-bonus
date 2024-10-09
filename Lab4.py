# Juniper Vermillo
# CIS 129
# 10/8/2024
# Lab4.py - Calculate the store bonus and the employee bonus based on the monthly amount and percentage increase of sales

def main():
    monthlySales = getSales()
    salesIncrease = getIncrease()
    empAmount = calcEmpBonus(salesIncrease)
    storeAmount = calcStoreBonus(monthlySales)
    printBonus(storeAmount, empAmount)

# Calculate monthly sales
def getSales():
    monthlySales = float(input("What are the monthly Sales? "))
    return monthlySales

# Calculate percentage increase of sales
def getIncrease():
    salesIncrease = float(input("Sales increased by what percent? "))
    salesIncrease /= 100
    return salesIncrease # Determines storeAmount bonus

# Calculate montly sales bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# Calculate employee amount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# Print info about bonuses
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $" + str(storeAmount))
    print("The employee bonus amount is $" + str(empAmount))
    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible!")

# Calls main
main()