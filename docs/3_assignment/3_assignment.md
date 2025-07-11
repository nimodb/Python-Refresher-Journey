# Assignment 1: Purchase Calculation

This assignment involves writing a program to calculate how much money is left after buying an item with tax.

## Problem Description
- You start with $50.
- You buy an item that costs $15, with a 3% tax.
- Print how much money you have left after the purchase.

## Solution
See [src/3_assignment.py](../../src/3_assignment/3_assignment.py) for the full code.

The program:
1. Stores the initial money ($50) in a variable.
2. Calculates the tax (3% of $15) and adds it to the item cost.
3. Subtracts the total cost from the initial money.
4. Prints the remaining money.

```python
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
```

Output: `Money left after purchase: $34.55`