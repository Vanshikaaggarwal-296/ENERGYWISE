
import csv


def read_energy_data(filename):
    records = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {"date", "consumption_kwh"}

        if not reader.fieldnames or not required_columns.issubset(
            reader.fieldnames
        ):
            raise ValueError(
                "CSV must contain date and consumption_kwh columns."
            )

        for row in reader:
            try:
                consumption = float(row["consumption_kwh"])
            except (ValueError, TypeError):
                raise ValueError(
                    f"Invalid consumption value for date {row['date']}."
                )

            if consumption < 0:
                raise ValueError("Consumption cannot be negative.")

            records.append({
                "date": row["date"],
                "consumption_kwh": consumption
            })

    return records


# Run this test only when this file is executed directly
if __name__ == "__main__":
    data = read_energy_data("energy_data.csv")

    print("EnergyWise - Electricity Data")

    for record in data:
        print(
            record["date"],
            "-",
            record["consumption_kwh"],
            "kWh"
        )

    total = sum(record["consumption_kwh"] for record in data)

    print("\nTotal Consumption:", total, "kWh")
    print("Number of Records:", len(data))

