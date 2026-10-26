"""Generate explainable, scenario-based EnergyWise recommendations."""

import math
from rules import RULES


def _validate_number(name, value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a valid number.") from None
    if not math.isfinite(number):
        raise ValueError(f"{name} must be a finite number.")
    return number


def get_recommendations(
    baseline,
    tariff,
    general_reduction_percent,
    standby_reduction_percent,
):
    """Return estimated recommendations for monthly baseline kWh and tariff.

    The two scenarios are alternatives and may overlap; do not add their
    savings together unless a separate non-overlapping model is available.
    """
    baseline = _validate_number("Baseline", baseline)
    tariff = _validate_number("Tariff", tariff)
    general_reduction_percent = _validate_number(
        "General reduction percentage", general_reduction_percent
    )
    standby_reduction_percent = _validate_number(
        "Standby reduction percentage", standby_reduction_percent
    )

    if baseline <= 0:
        raise ValueError("Baseline must be greater than zero.")
    if tariff < 0:
        raise ValueError("Tariff cannot be negative.")
    for name, percent in (
        ("General reduction percentage", general_reduction_percent),
        ("Standby reduction percentage", standby_reduction_percent),
    ):
        if not 0 <= percent <= 100:
            raise ValueError(f"{name} must be between 0 and 100.")

    percentages = {
        "general_reduction_percent": general_reduction_percent,
        "standby_reduction_percent": standby_reduction_percent,
    }
    original_bill = baseline * tariff
    recommendations = []

    for rule in RULES:
        percent = percentages[rule["input_key"]]
        saved_units = baseline * percent / 100
        after_units = baseline - saved_units
        saved_money = saved_units * tariff
        recommendations.append({
            "id": rule["id"],
            "title": rule["title"],
            "action": rule["action_template"].format(percent=percent),
            "reduction_percent": percent,
            "baseline_kwh": round(baseline, 2),
            "estimated_units_saved": round(saved_units, 2),
            "estimated_consumption_after_kwh": round(after_units, 2),
            "estimated_bill_before": round(original_bill, 2),
            "estimated_bill_after": round(after_units * tariff, 2),
            "estimated_money_saved": round(saved_money, 2),
            "ease_score": rule["ease_score"],
            "ease_label": rule["ease_label"],
            "confidence": "Scenario-based",
            "evidence": rule["basis"],
            "assumption": (
                "Uses the entered reduction percentage and a flat tariff. "
                "Actual savings may differ; tariff slabs and fixed charges are not modelled."
            ),
        })

    return recommendations
