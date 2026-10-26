def calculate_bill(consumption, tariff):
    if consumption < 0 or tariff < 0:
        raise ValueError("Consumption and tariff cannot be negative.")


    return consumption * tariff


def calculate_savings(baseline, new_consumption, tariff):
    if baseline < 0 or new_consumption < 0 or tariff < 0:
        raise ValueError("Values cannot be negative.")


    saved_units = baseline - new_consumption
    saved_amount = saved_units * tariff

    return saved_units, saved_amount

def calculate_savings_percentage(baseline, new_consumption):
    if baseline <= 0:
        return 0


    percentage = ((baseline - new_consumption) / baseline) * 100
    return round(percentage, 2)


if __name__ == "__main__":
    bill = calculate_bill(520, 7)
    print("Estimated Electricity Bill: Rs.", bill)


    units, amount = calculate_savings(520, 478, 7)
    print("Electricity Saved:", units, "kWh")
    print("Estimated Money Saved: Rs.", amount)

    percentage = calculate_savings_percentage(520, 478)
    print("Electricity Savings Percentage:", percentage, "%")

