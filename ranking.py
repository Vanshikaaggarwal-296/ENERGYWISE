def rank_recommendations(recommendations):
    for item in recommendations:
        saving_score = item["saving_score"]
        ease_score = item["ease_score"]

        item["rank_score"] = (
            0.6 * saving_score
            + 0.4 * ease_score
        )

    ranked = sorted(
        recommendations,
        key=lambda item: item["rank_score"],
        reverse=True
    )

    return ranked

# Sample data for testing
sample_recommendations = [
    {
        "title": "Reduce standby power",
        "saving_score": 6,
        "ease_score": 9
    },
    {
        "title": "Review high energy usage",
        "saving_score": 9,
        "ease_score": 5
    },
    {
        "title": "Monitor electricity consumption",
        "saving_score": 4,
        "ease_score": 8
    }
]

ranked_items = rank_recommendations(sample_recommendations)

print("Ranked Energy-Saving Recommendations:")

for item in ranked_items:
    print(item["title"], "-", round(item["rank_score"], 2))