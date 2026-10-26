def simulate_savings(baseline, reduction_percent, tariff):

    if baseline <= 0:
        raise ValueError("Baseline must be greater than zero.")

    if reduction_percent < 0 or reduction_percent > 100:
        raise ValueError("Reduction must be between 0 and 100.")

    if tariff < 0:
        raise ValueError("Tariff cannot be negative.")

    saved_units = baseline * reduction_percent / 100

    new_consumption = baseline - saved_units

    baseline_bill = baseline * tariff

    new_bill = new_consumption * tariff

    estimated_savings = baseline_bill - new_bill

    return new_consumption, new_bill, estimated_savings


# Test the simulator
baseline = 520
reduction_percent = 10
tariff = 7

new_units, new_bill, savings = simulate_savings(
    baseline, reduction_percent, tariff
)

print("Original Consumption:", baseline, "kWh")
print("Target Reduction:", reduction_percent, "%")
print("New Estimated Consumption:", new_units, "kWh")
print("New Estimated Bill: Rs.", new_bill)
print("Estimated Savings: Rs.", savings)