depositAmount = float(input())
depositTerm = int(input())
anualInterestRate = float(input())

# срокът на депозита е 6 месеца, затова делим годишната лихва на 2
# и след това я делим на 100, за да я превърнем в десетично число
#interest = depositAmount * (anualInterestRate / 100) / 2
#finalAmount = depositAmount + interest

# по-добре е да изчислим лихвата за 1 месец и след това да я умножим по броя на месеците
monthlyInterest = depositAmount * (anualInterestRate / 100) / 12
finalAmount = depositAmount + (monthlyInterest * depositTerm)
#print(monthlyInterest)
print(finalAmount)
