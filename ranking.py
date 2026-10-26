"""Rank recommendations by estimated impact and practical ease."""


def rank_recommendations(recommendations):
    """Rank by estimated money saved weighted by ease (score 1–5).

    This is a transparent prioritization heuristic, not a prediction model.
    """
    ranked = []
    for item in recommendations:
        if "estimated_money_saved" not in item:
            raise KeyError("Each recommendation needs estimated_money_saved.")

        saving = float(item["estimated_money_saved"])
        ease = float(item.get("ease_score", 3))
        if not 1 <= ease <= 5:
            raise ValueError("ease_score must be between 1 and 5.")

        ranked_item = dict(item)
        ranked_item["ranking_score"] = round(saving * ease / 5, 2)
        ranked.append(ranked_item)

    ranked.sort(
        key=lambda item: (
            item["ranking_score"],
            item["estimated_money_saved"],
            item.get("title", ""),
        ),
        reverse=True,
    )

    for index, item in enumerate(ranked, start=1):
        item["rank"] = index
        if item["estimated_money_saved"] <= 0:
            item["priority"] = "Low"
        elif index == 1:
            item["priority"] = "High"
        elif index == 2:
            item["priority"] = "Medium"
        else:
            item["priority"] = "Low"

    return ranked
