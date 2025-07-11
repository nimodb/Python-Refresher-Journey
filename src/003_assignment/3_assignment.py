# Starting money
money = 50
# Item cost and tax rate
item_cost = 15
tax_rate = 0.03
# Calculate tax and total cost
tax = item_cost * tax_rate
total_cost = item_cost + tax
# Calculate money left
money_left = money - total_cost
# Display result
print(f"Money left after purchase: ${money_left}")