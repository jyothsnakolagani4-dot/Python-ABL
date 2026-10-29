
"""
Case Study 4: Multi-Product Shopping Budget Constraint
Evaluates a shopping basket, applies discounts, and reduces quantities
until the total fits within the budget.
"""

print("MULTI-PRODUCT SHOPPING BUDGET PLANNER")

budget = float(input("Enter your shopping budget (Rs): "))

while budget < 0:
    print("Budget cannot be negative.")
    budget = float(input("Enter your shopping budget (Rs): "))

count = int(input("Enter number of different products: "))

while count <= 0:
    print("Please enter at least one product.")
    count = int(input("Enter number of different products: "))

products = []

for i in range(count):
    print("\nProduct", i + 1)

    name = input("Product name: ").strip()
    while not name:
        print("Product name cannot be empty.")
        name = input("Product name: ").strip()

    price = float(input("Unit price (Rs): "))
    while price < 0:
        print("Price cannot be negative.")
        price = float(input("Unit price (Rs): "))

    quantity = int(input("Quantity in just numbers: "))
    while quantity < 0:
        print("Quantity cannot be negative.")
        quantity = int(input("Quantity: "))

    products.append([name, price, quantity])

# Store the original basket
original = [item.copy() for item in products]

# Calculate original bill
original_subtotal = 0

for name, price, quantity in products:
    original_subtotal += price * quantity

if original_subtotal >= 5000:
    original_rate = 0.10
elif original_subtotal >= 2500:
    original_rate = 0.05
else:
    original_rate = 0.0

original_discount = original_subtotal * original_rate
original_total = original_subtotal - original_discount

print("\n--- ORIGINAL BASKET ---")

for name, price, quantity in original:
    print(name, ":", quantity, "x Rs", price,
          "= Rs", price * quantity)

print("Subtotal: Rs", round(original_subtotal, 2))
print("Discount rate:", original_rate * 100, "%")
print("Discount: Rs", round(original_discount, 2))
print("Total after discount: Rs", round(original_total, 2))
print("Budget: Rs", budget)

# Reduce quantities until the total fits the budget
reductions = []

subtotal = original_subtotal
discount = original_discount
final_total = original_total
rate = original_rate

while final_total > budget:
    candidates = []

    for item in products:
        if item[2] > 0:
            candidates.append(item)

    if len(candidates) == 0:
        break

    # Select the product with the highest unit price
    selected = candidates[0]

    for item in candidates:
        if item[1] > selected[1]:
            selected = item

    selected[2] -= 1
    reductions.append(selected[0])

    # Recalculate the bill
    subtotal = 0

    for name, price, quantity in products:
        subtotal += price * quantity

    if subtotal >= 5000:
        rate = 0.10
    elif subtotal >= 2500:
        rate = 0.05
    else:
        rate = 0.0

    discount = subtotal * rate
    final_total = subtotal - discount

# Display recommended basket
print("\n--- RECOMMENDED BASKET ---")

for name, price, quantity in products:
    print(name, ":", quantity, "x Rs", price,
          "= Rs", price * quantity)

print("Revised subtotal: Rs", round(subtotal, 2))
print("Discount rate:", rate * 100, "%")
print("Discount: Rs", round(discount, 2))
print("Final total: Rs", round(final_total, 2))
print("Money remaining: Rs", round(budget - final_total, 2))

if reductions:
    print("\nQuantity reductions made:")

    for name in reductions:
        print("- Removed one unit of", name)
else:
    print("\nOriginal basket is already within budget.")

if final_total <= budget:
    print("Status: Basket fits within budget.")
else:
    print("Status: Unable to fit the basket within budget.")
