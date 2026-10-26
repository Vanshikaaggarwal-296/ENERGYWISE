def calculate_bill(consumption, tariff):
    bill = consumption * tariff
    return bill


def calculate_savings(baseline, new_consumption, tariff):
    saved_units = baseline - new_consumption
    saved_amount = saved_units * tariff

    return saved_units, saved_amount
# Test 1: Calculate electricity bill
bill = calculate_bill(520, 7)
print("Estimated Electricity Bill: ₹", bill)

# Test 2: Calculate electricity savings
units, amount = calculate_savings(520, 478, 7)

print("Electricity Units Saved:", units, "kWh")
print("Estimated Money Saved: ₹", amount)