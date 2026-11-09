# REFLECTION 1:
# I would use .get() when a key might not exist because it lets me
# provide a default value instead of getting an error. I would use
# bracket notation when I know the key exists and need its value.
# My rule of thumb is to use .get() for optional information and
# brackets for information that should always be there.

# REFLECTION 2:
# This pattern reminds me of using SUMIF in Excel because it adds
# values based on a matching category. Python is more useful for
# large datasets because it can process many records automatically
# and can handle more complicated calculations.


# EXERCISE 1 - One customer

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print("EXERCISE 1")

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# EXERCISE 2 - Update and add

print("\nEXERCISE 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3 - Safe lookup

print("\nEXERCISE 3")

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# EXERCISE 4 - Iterate

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the keys,
# not both the keys and their values.

for key in customer:
    print(key)


# EXERCISE 5 - Lookup table

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount_rate = tier_discounts.get(customer["tier"], 0)

purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print("Tier:", customer["tier"])
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", round(final_price, 2))


# EXERCISE 6 - List of dictionaries

print("\nEXERCISE 6")

dict1 = customer.copy()

dict2 = {
    "name": "Bob",
    "tier": "silver",
    "ytd_spend": 800
}

dict3 = {
    "name": "Charlie",
    "tier": "bronze",
    "ytd_spend": 400
}

customers = [dict1, dict2, dict3]

for person in customers:
    discount_rate = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * discount_rate

    print(
        f'{person["name"]} | '
        f'Tier: {person["tier"]} | '
        f'Discount: ${discount_amount:.2f}'
    )


# EXERCISE 7 - Nested catalog

print("\nEXERCISE 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")


# EXERCISE 8 - Sales by region

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
