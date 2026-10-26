def get_recommendations(consumption):
    recommendations = []

    if consumption > 400:
        recommendations.append({
            "title": "Review High Energy Consumption",
            "message": "Check your electricity usage patterns.",
            "priority": "High"
        })

    if consumption > 200:
        recommendations.append({
            "title": "Reduce Standby Power",
            "message": "Switch off devices when not in use.",
            "priority": "Medium"
        })

    if consumption <= 200:
        recommendations.append({
            "title": "Maintain Efficient Usage",
            "message": "Continue monitoring your electricity usage.",
            "priority": "Low"
        })

    return recommendations


# Test the recommendation engine
results = get_recommendations(520)

for item in results:
    print("\nRecommendation:", item["title"])
    print("Action:", item["message"])
    print("Priority:", item["priority"])