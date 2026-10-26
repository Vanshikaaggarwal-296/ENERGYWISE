
from recommendation import get_recommendations
from ranking import rank_recommendations


# Test 1: Generate recommendations
recommendations = get_recommendations(520, 7)

assert len(recommendations) == 2
print("Recommendation generation: PASS")


# Test 2: Check savings calculations
assert recommendations[0]["estimated_units_saved"] == 26.0
assert recommendations[0]["estimated_money_saved"] == 182.0
print("Savings calculation: PASS")


# Test 3: Check ranking
ranked = rank_recommendations(recommendations)

assert ranked[0]["estimated_money_saved"] >= ranked[1]["estimated_money_saved"]
print("Recommendation ranking: PASS")


# Display final ranking
print("\n===== TEST RESULTS =====")

for item in ranked:
    print(
        item["title"],
        "| Estimated Savings: Rs.",
        item["estimated_money_saved"]
    )
