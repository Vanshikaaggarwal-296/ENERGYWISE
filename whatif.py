"""What-if electricity saving simulator."""

import math


def _finite_number(name, value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a valid number.") from None
    if not math.isfinite(number):
        raise ValueError(f"{name} must be a finite number.")
    return number


def simulate_savings(baseline, reduction_percent, tariff):
    baseline = _finite_number("Baseline", baseline)
    reduction_percent = _finite_number("Reduction percentage", reduction_percent)
    tariff = _finite_number("Tariff", tariff)

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

    return (
        round(new_consumption, 2),
        round(new_bill, 2),
        round(estimated_savings, 2),
    )
