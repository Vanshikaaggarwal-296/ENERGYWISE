
from recommendation import get_recommendations
from ranking import rank_recommendations

# Example monthly consumption and tariff
consumption = 520
tariff = 7

# Generate recommendations
recommendations = get_recommendations(consumption, tariff)

# Rank recommendations
ranked_recommendations = rank_recommendations(recommendations)

# Display results
print("\n===== ENERGYWISE SMART RECOMMENDATIONS =====")

for item in ranked_recommendations:
    print("\nRecommendation:", item["title"])
    print("Action:", item["action"])
    print("Estimated Units Saved:", item["estimated_units_saved"], "kWh")
    print("Estimated Money Saved: Rs.", item["estimated_money_saved"])
    print("Priority:", item["priority"])
    print("Ranking Score:", item["rank_score"])
    print("Evidence:", item["evidence"])

