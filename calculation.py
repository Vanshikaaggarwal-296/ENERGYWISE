
def calculate_bill(consumption, tariff):
    if consumption < 0 or tariff < 0:
        raise ValueError("Consumption and tariff cannot be negative.")

    bill = consumption * tariff
    return bill


def calculate_savings(baseline, new_consumption, tariff):
    if baseline < 0 or new_consumption < 0 or tariff < 0:
        raise ValueError("Values cannot be negative.")

    if new_consumption > baseline:
        saved_units = baseline - new_consumption
        saved_amount = saved_units * tariff
        return saved_units, saved_amount

    saved_units = baseline - new_consumption
    saved_amount = saved_units * tariff

    return saved_units, saved_amount


# Test the functions
bill = calculate_bill(520, 7)
print("Estimated Electricity Bill: ₹", bill)

units, amount = calculate_savings(520, 478, 7)
print("Electricity Units Saved:", units, "kWh")
print("Estimated Money Saved: ₹", amount)

