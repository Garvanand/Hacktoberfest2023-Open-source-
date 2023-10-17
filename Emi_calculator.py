p = float(input("Enter principal: "))
R = float(input("Enter  interest rate: "))
n = int(input("Enter number of month: " ))

r = R/(12*100)

emi = p * r * ((1+r)**n)/((1+r)**n - 1)

print("Monthly installmenrt = ", emi)
