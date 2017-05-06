p = int(input("Enter principal amount "))

d = int(input("Enter discoutnt percent "))

dis = ((p*d)/100)
if dis < 250:
    payable_amount = p-dis
else:
    payable_amount = p-250
print(payable_amount)
