from data_reader import read_energy_data
from calculation import calculate_bill

# Read electricity data from CSV
data = read_energy_data("energy_data.csv")

# Calculate total consumption
total_consumption = sum(
    record["consumption_kwh"] for record in data
)

# Calculate daily average
if len(data) > 0:
    daily_average = total_consumption / len(data)
else:
    daily_average = 0

# Electricity tariff (example rate)
tariff = 7

# Estimate electricity cost
estimated_bill = calculate_bill(total_consumption, tariff)

# Display results
print("\n===== ENERGYWISE ANALYSIS =====")
print("Total Consumption:", total_consumption, "kWh")
print("Number of Days:", len(data))
print("Daily Average:", round(daily_average, 2), "kWh")
print("Estimated Cost: Rs.", estimated_bill)

# Find the day with the highest electricity consumption
if data:
    highest_day = max(
        data,
        key=lambda record: record["consumption_kwh"]
    )

    print("\n===== DAILY CONSUMPTION INSIGHTS =====")

    print(
        "Highest Consumption Day:",
        highest_day["date"]
    )

    print(
        "Highest Daily Usage:",
        highest_day["consumption_kwh"],
        "kWh"
    )

    print("\nDaily Usage Report:")

    for record in data:
        print(
            record["date"],
            "->",
            record["consumption_kwh"],
            "kWh"
        )
else:
    print("No electricity data available.")


# Detect unusually high daily consumption
if len(data) >= 2:
    average_usage = sum(
        record["consumption_kwh"] for record in data
    ) / len(data)

    threshold = average_usage * 1.2

    print("\n===== UNUSUAL USAGE CHECK =====")
    print("Average Daily Usage:", round(average_usage, 2), "kWh")

    unusual_days = [
        record for record in data
        if record["consumption_kwh"] > threshold
    ]

    if unusual_days:
        for record in unusual_days:
            print(
                "Unusually High Usage:",
                record["date"],
                "-",
                record["consumption_kwh"],
                "kWh"
            )
    else:
        print("No unusually high usage detected.")
else:
    print("Not enough data to detect unusual usage.")

