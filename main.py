
from data_reader import read_energy_data
from recommendation import get_recommendations
from ranking import rank_recommendations
from whatif import simulate_savings


def main():
    print("===== ENERGYWISE SMART SAVING ASSISTANT =====")

    try:
        # Read electricity data from CSV
        data = read_energy_data("energy_data.csv")

        if not data:
            print("No electricity data found.")
            return

        # Calculate total consumption and daily average
        total_consumption = sum(
            record["consumption_kwh"] for record in data
        )

        daily_average = total_consumption / len(data)

        # Estimate monthly usage from the available daily average
        monthly_consumption = daily_average * 30
        tariff = 7

        print("\n===== CONSUMPTION SUMMARY =====")
        print("Records:", len(data), "days")
        print("Total Recorded Usage:", round(total_consumption, 2), "kWh")
        print("Daily Average:", round(daily_average, 2), "kWh")
        print(
            "Estimated Monthly Usage:",
            round(monthly_consumption, 2),
            "kWh"
        )

        # Generate and rank recommendations
        recommendations = get_recommendations(
            monthly_consumption, tariff
        )
        ranked = rank_recommendations(recommendations)

        print("\n===== SAVING RECOMMENDATIONS =====")

        for item in ranked:
            print("\nRecommendation:", item["title"])
            print("Action:", item["action"])
            print(
                "Estimated Units Saved:",
                item["estimated_units_saved"],
                "kWh"
            )
            print(
                "Estimated Money Saved: Rs.",
                item["estimated_money_saved"]
            )
            print("Priority:", item["priority"])

        # Run what-if simulation
        reduction = float(
            input("\nEnter a target reduction percentage (0-100): ")
        )

        new_units, new_bill, savings = simulate_savings(
            monthly_consumption, reduction, tariff
        )

        print("\n===== WHAT-IF SIMULATION =====")
        print(
            "Estimated Monthly Usage Before:",
            round(monthly_consumption, 2),
            "kWh"
        )
        print("Estimated Usage After:", round(new_units, 2), "kWh")
        print("Estimated Bill After: Rs.", round(new_bill, 2))
        print("Estimated Savings: Rs.", round(savings, 2))

        print(
            "\nNote: Monthly usage is extrapolated from sample daily data. "
            "Actual consumption and savings may differ."
        )

    except (ValueError, KeyError, OSError) as error:
        print("Unable to process energy data:", error)


if __name__ == "__main__":
    main()

