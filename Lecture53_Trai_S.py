def vatCalculator(totalPrice = float(input("Price : "))):
    result = totalPrice*107/100
    return result

print(vatCalculator())
