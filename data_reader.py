import csv


def read_energy_data(filename):
    records = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            consumption = float(row["consumption_kwh"])

            if consumption < 0:
                raise ValueError("Consumption cannot be negative.")

            records.append({
                "date": row["date"],
                "consumption_kwh": consumption
            })

    return records


# Test the CSV reader
data = read_energy_data("energy_data.csv")

print("EnergyWise - Electricity Data")

for record in data:
    print(record["date"], "-", record["consumption_kwh"], "kWh")

total = sum(record["consumption_kwh"] for record in data)

print("\nTotal Consumption:", total, "kWh")
print("Number of Records:", len(data))