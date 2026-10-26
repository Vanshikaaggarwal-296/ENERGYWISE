def get_recommendations(
    baseline,
    tariff,
    general_reduction_percent,
    standby_reduction_percent
):
    if baseline <= 0:
        raise ValueError("Baseline must be greater than zero.")

    if tariff < 0:
        raise ValueError("Tariff cannot be negative.")

    if not 0 <= general_reduction_percent <= 100:
        raise ValueError(
            "General reduction must be between 0 and 100."
        )

    if not 0 <= standby_reduction_percent <= 100:
        raise ValueError(
            "Standby reduction must be between 0 and 100."
        )

    recommendations = []

    # Recommendation 1: Overall electricity consumption
    saved_units = (
        baseline * general_reduction_percent / 100
    )

    saved_money = saved_units * tariff

    recommendations.append({
        "title": "Reduce Electricity Consumption",
        "action": (
            f"Try reducing overall electricity usage "
            f"by {general_reduction_percent}%."
        ),
        "estimated_units_saved": round(saved_units, 2),
        "estimated_money_saved": round(saved_money, 2),
        "evidence": (
            f"Estimated using a {general_reduction_percent}% "
            "user-selected reduction scenario."
        )
    })

    # Recommendation 2: Standby power reduction
    saved_units = (
        baseline * standby_reduction_percent / 100
    )

    saved_money = saved_units * tariff

    recommendations.append({
        "title": "Reduce Standby Power",
        "action": (
            "Switch off devices when they are not in use. "
            f"Target reduction: {standby_reduction_percent}%."
        ),
        "estimated_units_saved": round(saved_units, 2),
        "estimated_money_saved": round(saved_money, 2),
        "evidence": (
            f"Estimated using a {standby_reduction_percent}% "
            "user-selected reduction scenario."
        )
    })

    return recommendations