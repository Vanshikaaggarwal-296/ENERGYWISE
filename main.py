
from recommendation import get_recommendations
from ranking import rank_recommendations
from whatif import simulate_savings


def main():
    print("===== ENERGYWISE SMART SAVING ASSISTANT =====")

    try:
        consumption = float(input("Enter monthly consumption (kWh): "))
        tariff = float(input("Enter electricity tariff (Rs./kWh): "))

        if consumption <= 0 or tariff < 0:
            print("Consumption must be positive and tariff cannot be negative.")
            return

        # Generate and rank recommendations
        recommendations = get_recommendations(consumption, tariff)
        ranked = rank_recommendations(recommendations)

        print("\n===== SAVING RECOMMENDATIONS =====")

        for item in ranked:
            print("\nRecommendation:", item["title"])
            print("Action:", item["action"])
            print("Estimated Units Saved:", item["estimated_units_saved"], "kWh")
            print("Estimated Money Saved: Rs.", item["estimated_money_saved"])
            print("Priority:", item["priority"])

        # Run the what-if simulation
        reduction = float(input("\nEnter a target reduction percentage (0-100): "))

        new_units, new_bill, savings = simulate_savings(
            consumption, reduction, tariff
        )

        print("\n===== WHAT-IF SIMULATION =====")
        print("Original Consumption:", consumption, "kWh")
        print("Estimated New Consumption:", round(new_units, 2), "kWh")
        print("Estimated New Bill: Rs.", round(new_bill, 2))
        print("Estimated Savings: Rs.", round(savings, 2))

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()

