
def get_recommendations(baseline, tariff=7):
    recommendations = []

    if baseline <= 0:
        return recommendations

    # Recommendation 1: Reduce electricity consumption
    reduction_percent = 5
    saved_units = baseline * reduction_percent / 100
    saved_money = saved_units * tariff

    recommendations.append({
        "title": "Reduce Electricity Consumption",
        "action": "Try reducing overall electricity usage by 5%.",
        "estimated_units_saved": round(saved_units, 2),
        "estimated_money_saved": round(saved_money, 2),
        "evidence": "Illustrative 5% reduction scenario",
        "priority": "High"
    })

    # Recommendation 2: Reduce standby power
    reduction_percent = 2
    saved_units = baseline * reduction_percent / 100
    saved_money = saved_units * tariff

    recommendations.append({
        "title": "Reduce Standby Power",
        "action": "Switch off devices when they are not in use.",
        "estimated_units_saved": round(saved_units, 2),
        "estimated_money_saved": round(saved_money, 2),
        "evidence": "Illustrative 2% reduction scenario",
        "priority": "Medium"
    })

    return recommendations


# Test the recommendation engine
if __name__ == "__main__":
    results = get_recommendations(520, 7)

    print("===== ENERGYWISE SAVING RECOMMENDATIONS =====")

    for item in results:
        print("\nRecommendation:", item["title"])
        print("Action:", item["action"])
        print("Estimated Units Saved:", item["estimated_units_saved"], "kWh")
        print("Estimated Money Saved: Rs.", item["estimated_money_saved"])
        print("Evidence:", item["evidence"])
        print("Priority:", item["priority"])

