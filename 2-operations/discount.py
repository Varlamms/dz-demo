price = input()
discount = input()

discount_amount = int(price) * (int(discount) / 100)

print(int(price) - int(discount_amount))
