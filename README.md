# EnergyWise — Smart Energy Saving Assistant

## Project Overview

EnergyWise is a smart energy usage and saving assistant that analyzes electricity consumption data and estimates potential savings through transparent, user-configurable scenarios.

The system summarizes consumption, generates energy-saving recommendations, ranks them, and simulates possible changes in electricity usage.

## My Contribution

**Role:** Savings & Recommendation Engine
**Contributor:** Vanshika Aggarwal

My responsibilities include:

* Calculating estimated electricity consumption, bills, and savings.
* Generating scenario-based energy-saving recommendations.
* Ranking recommendations using estimated monetary savings and ease of implementation.
* Simulating electricity-consumption reduction scenarios.
* Working with CSV-based electricity consumption data.
* Validating inputs and testing calculations, recommendations, and simulations.

## Key Features

* Daily average and estimated 30-day electricity consumption.
* Estimated electricity bill based on a user-provided tariff.
* Dynamic energy-saving recommendations.
* Recommendation ranking using a transparent scoring heuristic.
* What-if simulation for different reduction percentages.
* Input validation and error handling.
* Automated tests for recommendation calculations and edge cases.

## Technologies Used

* Python
* CSV
* Git and GitHub
* Python `unittest` framework

## How to Run

1. Install Python.

2. Clone or download the EnergyWise repository.

3. Open the project directory in a terminal.

4. Run the application:

   ```bash
   python main.py
   ```

5. Enter the electricity tariff and requested reduction percentages.

6. Review the consumption summary, ranked recommendations, and what-if simulation.

## Recommendation and Ranking Logic

Recommendations calculate estimated energy savings from user-selected reduction percentages.

The ranking module considers estimated monetary savings and an ease score. Its ranking score is a transparent heuristic, not a machine-learning prediction.

Each recommendation includes its estimated impact and relevant assumptions.

## Sample Data and Assumptions

The included CSV contains sample electricity-consumption records for seven days.

Estimated monthly consumption is calculated by multiplying average daily consumption by 30. This is an extrapolation, not a measurement of a complete month's usage.

The application uses a user-provided electricity tariff and a simplified flat-rate calculation. Actual bills may differ due to tariff slabs, fixed charges, taxes, and real consumption patterns.

Recommendation percentages are user-selected scenarios, not measured or guaranteed savings. Different recommendations may overlap, so their estimated savings should not automatically be added together.

## Testing

Run the recommendation tests:

```bash
python -m unittest test_recommendation.py -v
```

Run the complete test discovery:

```bash
python -m unittest discover -v
```

Individual test scripts may also be available:

```bash
python test_calculation.py
python test_whatif.py
```

## Team

**Team Name:** InnovateX

**Project:** EnergyWise — Smart Energy Usage and Saving Assistant

**Contributor:** Vanshika Aggarwal
