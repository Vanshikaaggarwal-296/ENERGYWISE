
def rank_recommendations(recommendations):
    for item in recommendations:
        saving = item["estimated_money_saved"]

        # Higher estimated savings get a higher score.
        item["rank_score"] = saving

    ranked = sorted(
        recommendations,
        key=lambda item: item["rank_score"],
        reverse=True
    )

    return ranked
