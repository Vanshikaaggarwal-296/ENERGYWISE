from data_reader import read_energy_data
from recommendation import get_recommendations
from ranking import rank_recommendations
from whatif import simulate_savings


def get_percentage(prompt):
    """Get and validate a percentage from the user."""
    percentage = float(input(prompt))

    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    return percentage


def main():
    print("=" * 50)
    print("     ENERGYWISE SMART SAVING ASSISTANT")
    print("=" * 50)

    try:
        # Step 1: Read electricity data from CSV
        data = read_energy_data("energy_data.csv")

        if not data:
            print("No electricity data found.")
            return

        # Step 2: Calculate consumption from CSV data
        total_consumption = sum(
            record["consumption_kwh"] for record in data
        )

        if total_consumption < 0:
            raise ValueError("Consumption cannot be negative.")

        if any(record["consumption_kwh"] < 0 for record in data):
            raise ValueError("Consumption values cannot be negative.")

        daily_average = total_consumption / len(data)
        monthly_consumption = daily_average * 30

        # Step 3: Take electricity tariff from user
        print("\n===== ENTER YOUR DETAILS =====")

        tariff = float(
            input("Enter electricity tariff (Rs./kWh): ")
        )

        if tariff < 0:
            raise ValueError("Tariff cannot be negative.")

        # Step 4: Take recommendation percentages from user
        general_reduction = get_percentage(
            "Enter overall usage reduction percentage (0-100): "
        )

        standby_reduction = get_percentage(
            "Enter standby power reduction percentage (0-100): "
        )

        # Step 5: Display consumption summary
        print("\n===== CONSUMPTION SUMMARY =====")

        print("Records:", len(data), "days")
        print(
            "Total Recorded Usage:",
            round(total_consumption, 2),
            "kWh"
        )
        print(
            "Daily Average:",
            round(daily_average, 2),
            "kWh"
        )
        print(
            "Estimated Monthly Usage:",
            round(monthly_consumption, 2),
            "kWh"
        )
        print("Electricity Tariff: Rs.", tariff, "per kWh")

        # Step 6: Generate dynamic recommendations
        recommendations = get_recommendations(
            monthly_consumption,
            tariff,
            general_reduction,
            standby_reduction
        )

        # Step 7: Rank recommendations by estimated money saved
        ranked = rank_recommendations(recommendations)

        print("\n===== SAVING RECOMMENDATIONS =====")

        for item in ranked:
            print("\nRank:", item["rank"])
            print("Recommendation:", item["title"])
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

        # Step 8: Take input for what-if simulation
        reduction = get_percentage(
            "\nEnter target reduction for what-if simulation (0-100): "
        )

        # Step 9: Calculate what-if savings
        new_units, new_bill, savings = simulate_savings(
            monthly_consumption,
            reduction,
            tariff
        )

        print("\n===== WHAT-IF SIMULATION =====")

        print(
            "Estimated Monthly Usage Before:",
            round(monthly_consumption, 2),
            "kWh"
        )

        print(
            "Estimated Monthly Usage After:",
            round(new_units, 2),
            "kWh"
        )

        print("Estimated Bill After: Rs.", round(new_bill, 2))
        print("Estimated Savings: Rs.", round(savings, 2))

        # Step 10: Display calculation note
        print("\n===== IMPORTANT NOTE =====")
        print(
            "Monthly usage is estimated using the average "
            "of the available daily CSV records."
        )
        print(
            "Savings are estimates based on the percentages "
            "entered by the user."
        )
        print(
            "Actual electricity bills may differ due to "
            "fixed charges, tariff slabs and actual usage."
        )

    except (ValueError, KeyError, OSError) as error:
        print("\nUnable to process energy data:", error)


if __name__ == "__main__":
    main()