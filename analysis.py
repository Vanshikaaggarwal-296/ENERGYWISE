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