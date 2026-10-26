
def simulate_savings(baseline, reduction_percent, tariff=7):
    if baseline <= 0:
        raise ValueError("Baseline must be greater than zero.")

    if not 0 <= reduction_percent <= 100:
        raise ValueError("Reduction must be between 0 and 100.")

    if tariff < 0:
        raise ValueError("Tariff cannot be negative.")

    saved_units = baseline * reduction_percent / 100
    new_consumption = baseline - saved_units

    original_bill = baseline * tariff
    new_bill = new_consumption * tariff

    estimated_savings = original_bill - new_bill

    return new_consumption, new_bill, estimated_savings


# Run an interactive What-If simulation
if __name__ == "__main__":
    try:
        baseline = float(input("Enter monthly consumption (kWh): "))
        reduction = float(input("Enter target reduction (%): "))
        tariff = float(input("Enter electricity tariff (Rs./kWh): "))

        new_units, new_bill, savings = simulate_savings(
            baseline, reduction, tariff
        )

        print("\n===== ENERGYWISE WHAT-IF SIMULATOR =====")
        print("Original Consumption:", baseline, "kWh")
        print("Target Reduction:", reduction, "%")
        print("Estimated New Consumption:", round(new_units, 2), "kWh")
        print("Estimated New Bill: Rs.", round(new_bill, 2))
        print("Estimated Savings: Rs.", round(savings, 2))

    except ValueError as error:
        print("Invalid input:", error)

