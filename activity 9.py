# Case Study 9: Tuple-Based Product Catalogue Audit
# Topic 49 - Uses tuples, lists, loops, conditions, and tuple unpacking.

print("=" * 60)
print("           TUPLE-BASED PRODUCT CATALOGUE AUDIT")
print("=" * 60)

while True:
    try:
        product_count = int(input("Enter number of product records: "))
        if product_count > 0:
            break
        print("Enter a positive whole number.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

while True:
    try:
        reorder_level = int(input("Enter minimum stock level (reorder threshold): "))
        if reorder_level >= 0:
            break
        print("Stock threshold cannot be negative.")
    except ValueError:
        print("Invalid input. Enter a whole number.")

products = []
for i in range(product_count):
    print(f"\nProduct record {i + 1}")
    product_id = input("Product ID: ").strip()
    while product_id == "":
        print("Product ID cannot be empty.")
        product_id = input("Product ID: ").strip()

    name = input("Product name: ").strip()
    while name == "":
        print("Product name cannot be empty.")
        name = input("Product name: ").strip()

    while True:
        try:
            price = float(input("Unit price (Rs): "))
            break
        except ValueError:
            print("Invalid price. Enter a number.")

    while True:
        try:
            quantity = int(input("Stock quantity: "))
            break
        except ValueError:
            print("Invalid quantity. Enter a whole number.")

    # Each catalogue record is stored as an immutable tuple.
    products.append((product_id, name, price, quantity))

valid_products = []
invalid_products = []
seen_ids = []

for product in products:
    product_id, name, price, quantity = product  # Tuple unpacking
    errors = []

    if product_id in seen_ids:
        errors.append("duplicate product ID")
    else:
        seen_ids.append(product_id)

    if price <= 0:
        errors.append("price must be greater than zero")
    if quantity < 0:
        errors.append("quantity cannot be negative")

    if errors:
        invalid_products.append((product, ", ".join(errors)))
    else:
        valid_products.append(product)

print("\n" + "=" * 76)
print("VALID PRODUCT CATALOGUE")
print("=" * 76)
print(f"{'ID':<12}{'Product':<22}{'Price (Rs)':>14}{'Stock':>10}{'Value (Rs)':>16}")
print("-" * 76)

total_inventory_value = 0
reorder_products = []

for product in valid_products:
    product_id, name, price, quantity = product
    inventory_value = price * quantity
    total_inventory_value += inventory_value
    print(f"{product_id:<12}{name:<22}{price:>14.2f}{quantity:>10}{inventory_value:>16.2f}")

    if quantity < reorder_level:
        reorder_products.append(product)

print("-" * 76)
print(f"Total valid inventory value: Rs {total_inventory_value:.2f}")

print(f"\nPRODUCTS REQUIRING REPLENISHMENT (stock below {reorder_level})")
if reorder_products:
    for product in reorder_products:
        product_id, name, price, quantity = product
        print(f"- {product_id} | {name} | Current stock: {quantity}")
else:
    print("None")

print("\nINVALID PRODUCT RECORDS")
if invalid_products:
    for product, reason in invalid_products:
        product_id, name, price, quantity = product
        print(f"- {product_id} | {name}: {reason}")
else:
    print("None")

print("\nAUDIT SUMMARY")
print(f"Total records entered: {len(products)}")
print(f"Valid records: {len(valid_products)}")
print(f"Invalid records: {len(invalid_products)}")
print(f"Products needing replenishment: {len(reorder_products)}")
print("\nCatalogue audit complete.")