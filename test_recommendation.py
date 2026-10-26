
import unittest

from recommendation import get_recommendations
from ranking import rank_recommendations


class TestRecommendations(unittest.TestCase):

    def test_recommendation_generation(self):
        recommendations = get_recommendations(
            520, 7, 5, 2
        )

        self.assertEqual(len(recommendations), 2)

    def test_general_savings_calculation(self):
        recommendations = get_recommendations(
            520, 7, 10, 2
        )

        general = recommendations[0]

        self.assertEqual(
            general["estimated_units_saved"], 52.0
        )

        self.assertEqual(
            general["estimated_money_saved"], 364.0
        )

    def test_standby_savings_calculation(self):
        recommendations = get_recommendations(
            520, 7, 5, 4
        )

        standby = recommendations[1]

        self.assertEqual(
            standby["estimated_units_saved"], 20.8
        )

        self.assertEqual(
            standby["estimated_money_saved"], 145.6
        )

    def test_ranking(self):
        recommendations = get_recommendations(
            520, 7, 5, 2
        )

        ranked = rank_recommendations(recommendations)

        self.assertEqual(ranked[0]["priority"], "High")
        self.assertEqual(ranked[1]["priority"], "Medium")

        self.assertGreaterEqual(
            ranked[0]["estimated_money_saved"],
            ranked[1]["estimated_money_saved"]
        )

    def test_invalid_baseline(self):
        with self.assertRaises(ValueError):
            get_recommendations(0, 7, 5, 2)

    def test_invalid_tariff(self):
        with self.assertRaises(ValueError):
            get_recommendations(520, -1, 5, 2)

    def test_invalid_percentage(self):
        with self.assertRaises(ValueError):
            get_recommendations(520, 7, 101, 2)


if __name__ == "__main__":
    unittest.main()

