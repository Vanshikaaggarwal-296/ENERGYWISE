"""Command-line entry point for the EnergyWise individual prototype."""

import math
from data_reader import read_energy_data
from recommendation import get_recommendations
from ranking import rank_recommendations
from whatif import simulate_savings


def get_number(prompt):
    try:
        number = float(input(prompt))
    except (TypeError, ValueError):
        raise ValueError("Please enter a valid number.") from None
    if not math.isfinite(number):
        raise ValueError("Please enter a finite number.")
    return number


def get_percentage(prompt):
    percentage = get_number(prompt)
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")
    return percentage


def main():
    print("=" * 54)
    print("       ENERGYWISE | SMART SAVING ASSISTANT")
    print("=" * 54)

    try:
        data = read_energy_data("energy_data.csv")
        if not data:
            print("No electricity data found.")
            return

        if any(record["consumption_kwh"] < 0 for record in data):
            raise ValueError("Consumption values cannot be negative.")

        total_consumption = sum(record["consumption_kwh"] for record in data)
        daily_average = total_consumption / len(data)
        monthly_consumption = daily_average * 30

        print("\n===== YOUR INPUTS =====")
        tariff = get_number("Electricity tariff (Rs./kWh): ")
        if tariff < 0:
            raise ValueError("Tariff cannot be negative.")
        general_reduction = get_percentage("Overall reduction scenario (0-100%): ")
        standby_reduction = get_percentage("Standby reduction scenario (0-100%): ")

        print("\n===== CONSUMPTION BASELINE =====")
        print(f"CSV records: {len(data)} days")
        print(f"Recorded consumption: {total_consumption:.2f} kWh")
        print(f"Average daily consumption: {daily_average:.2f} kWh")
        print(f"Estimated 30-day consumption: {monthly_consumption:.2f} kWh")
        print(f"Estimated bill before savings: Rs. {monthly_consumption * tariff:.2f}")

        recommendations = get_recommendations(
            monthly_consumption, tariff, general_reduction, standby_reduction
        )
        ranked = rank_recommendations(recommendations)

        print("\n===== RANKED RECOMMENDATIONS =====")
        for item in ranked:
            print(f"\n#{item['rank']} | {item['priority']} priority | {item['title']}")
            print("Action:", item["action"])
            print(f"Estimated units saved: {item['estimated_units_saved']:.2f} kWh")
            print(f"Estimated bill after: Rs. {item['estimated_bill_after']:.2f}")
            print(f"Estimated money saved: Rs. {item['estimated_money_saved']:.2f}")
            print(
                f"Ease: {item['ease_label']} ({item['ease_score']}/5) | "
                f"Ranking score: {item['ranking_score']:.2f}"
            )
            print("Evidence:", item["evidence"])
            print("Confidence:", item["confidence"])
            print("Assumption:", item["assumption"])

        reduction = get_percentage("\nWhat-if target reduction (0-100%): ")
        new_units, new_bill, savings = simulate_savings(
            monthly_consumption, reduction, tariff
        )
        print("\n===== WHAT-IF SIMULATION =====")
        print(f"Target reduction: {reduction:.2f}%")
        print(f"Consumption before: {monthly_consumption:.2f} kWh")
        print(f"Consumption after: {new_units:.2f} kWh")
        print(f"Estimated bill after: Rs. {new_bill:.2f}")
        print(f"Estimated savings: Rs. {savings:.2f}")

        print("\n===== TRANSPARENCY NOTE =====")
        print("Monthly usage is extrapolated from the available daily CSV records.")
        print("Recommendation percentages are user-selected scenarios, not measured savings.")
        print("Recommendation scenarios may overlap; do not add their savings together.")
        print("The flat-tariff estimate excludes fixed charges and progressive tariff slabs.")

    except (ValueError, KeyError, OSError) as error:
        print("\nUnable to process energy data:", error)


if __name__ == "__main__":
    main()
