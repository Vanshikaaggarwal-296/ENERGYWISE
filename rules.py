"""Transparent recommendation rule definitions for EnergyWise.

Percentages are scenario inputs, not measured or guaranteed savings.
Ease is a simple 1–5 heuristic used only to prioritize practical actions.
"""

RULES = [
    {
        "id": "overall_reduction",
        "title": "Reduce Overall Electricity Consumption",
        "action_template": "Try reducing estimated monthly usage by {percent}%.",
        "input_key": "general_reduction_percent",
        "ease_score": 3,
        "ease_label": "Moderate",
        "basis": "User-selected overall reduction scenario; not measured appliance-level savings.",
    },
    {
        "id": "standby_reduction",
        "title": "Reduce Standby Power",
        "action_template": (
            "Switch off or unplug devices when practical; "
            "the selected scenario targets a {percent}% reduction."
        ),
        "input_key": "standby_reduction_percent",
        "ease_score": 4,
        "ease_label": "Easy",
        "basis": "User-selected standby reduction scenario; not measured standby-load data.",
    },
]
