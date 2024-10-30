def getPrice(amt):
    if amt > 2000:
        amt = amt * 0.9  # Apply 10% discount
    return int(amt)

print(getPrice(-11))
print(getPrice(180))
print(getPrice(2170))
print(getPrice(3100))
print(getPrice(9339))
print(getPrice(2001))