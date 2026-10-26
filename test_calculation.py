from calculation import calculate_bill, calculate_savings, calculate_savings_percentage


def test_calculate_bill():
    assert calculate_bill(520, 7) == 3640


def test_calculate_savings():
    units, amount = calculate_savings(520, 478, 7)

    assert units == 42
    assert amount == 294


def test_savings_percentage():
    percentage = calculate_savings_percentage(520, 478)

    assert percentage == 8.08


print("Bill calculation:", "PASS" if calculate_bill(520, 7) == 3640 else "FAIL")

units, amount = calculate_savings(520, 478, 7)
print("Savings calculation:", "PASS" if units == 42 and amount == 294 else "FAIL")

percentage = calculate_savings_percentage(520, 478)
print("Savings percentage:", "PASS" if percentage == 8.08 else "FAIL")