# EnergyWise — Smart Energy Saving Assistant

## Project Overview

EnergyWise is a smart energy usage and saving assistant that analyzes electricity consumption and provides estimated energy-saving recommendations.

## My Contribution

**Role: Savings & Recommendation Engine — Vanshika Aggarwal**

My responsibilities include:

* Calculating electricity bills and estimated savings.
* Generating energy-saving recommendations.
* Ranking recommendations by estimated monetary savings.
* Simulating different electricity consumption reduction scenarios.
* Reading electricity consumption data from CSV files.
* Testing calculations, recommendations, and simulations.

## Key Features

* Electricity bill estimation.
* Daily and estimated monthly consumption summaries.
* Energy-saving recommendations with priorities.
* Recommendation ranking.
* What-if savings simulation.
* CSV data validation.
* Automated tests for calculations and simulations.

## Technologies Used

* Python
* CSV
* Git and GitHub

## How to Run

1. Install Python.

2. Clone or download the EnergyWise repository.

3. Open the project folder in the terminal.

4. Run:

   `python main.py`

5. Enter the requested reduction percentage when prompted.

## Sample Data and Assumptions

The included CSV contains sample electricity consumption data for seven days. Monthly consumption is estimated by multiplying average daily usage by 30.

The example electricity tariff is ₹7 per kWh. Actual bills and savings may differ because of tariff slabs, fixed charges, real consumption patterns, and other factors.

Recommendations and savings figures are estimates, not guaranteed results.

## Testing

Run the following commands separately:

* `python test_calculation.py`
* `python test_recommendation.py`
* `python test_whatif.py`

## Team

**Team Name:** InnovateX

**Project:** EnergyWise — Smart Energy Usage and Saving Assistant
