from recommendation import get_recommendations
from ranking import rank_recommendations

# Test 1: High electricity consumption
recommendations = get_recommendations(520)

assert len(recommendations) > 0
print("Recommendation generation: PASS")

# Test 2: Check required information
for item in recommendations:
    assert "title" in item
    assert "message" in item
    assert "saving_score" in item
    assert "ease_score" in item

print("Recommendation details: PASS")

# Test 3: Check ranking
ranked = rank_recommendations(recommendations)

scores = [item["rank_score"] for item in ranked]
assert scores == sorted(scores, reverse=True)

print("Recommendation ranking: PASS")

# Display final recommendations
print("\nEnergyWise Recommendations:")

for item in ranked:
    print(
        item["title"],
        "| Score:",
        round(item["rank_score"], 2)
    )