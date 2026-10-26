
def rank_recommendations(recommendations):
    ranked = sorted(
        recommendations,
        key=lambda item: item["estimated_money_saved"],
        reverse=True
    )

    for index, item in enumerate(ranked):
        item["rank"] = index + 1

        if index == 0:
            item["priority"] = "High"
        elif index == 1:
            item["priority"] = "Medium"
        else:
            item["priority"] = "Low"

    return ranked

