import unittest

from recommendation import get_recommendations
from ranking import rank_recommendations


class TestRecommendations(unittest.TestCase):
    def test_creates_two_recommendations(self):
        self.assertEqual(len(get_recommendations(520, 7, 5, 2)), 2)

    def test_general_savings_calculation(self):
        item = get_recommendations(520, 7, 10, 2)[0]
        self.assertEqual(item["estimated_units_saved"], 52.0)
        self.assertEqual(item["estimated_money_saved"], 364.0)
        self.assertEqual(item["estimated_bill_after"], 3276.0)

    def test_standby_savings_calculation(self):
        item = get_recommendations(520, 7, 5, 4)[1]
        self.assertEqual(item["estimated_units_saved"], 20.8)
        self.assertEqual(item["estimated_money_saved"], 145.6)

    def test_exposes_evidence_and_assumptions(self):
        item = get_recommendations(520, 7, 5, 2)[0]
        self.assertIn("not measured", item["evidence"])
        self.assertIn("flat tariff", item["assumption"])
        self.assertEqual(item["confidence"], "Scenario-based")

    def test_zero_tariff_is_valid(self):
        items = get_recommendations(520, 0, 5, 2)
        self.assertEqual(items[0]["estimated_money_saved"], 0)

    def test_zero_reduction_is_valid(self):
        items = get_recommendations(520, 7, 0, 0)
        self.assertEqual(items[0]["estimated_units_saved"], 0)
        self.assertEqual(items[1]["estimated_money_saved"], 0)

    def test_100_percent_reduction_is_valid(self):
        item = get_recommendations(520, 7, 100, 2)[0]
        self.assertEqual(item["estimated_consumption_after_kwh"], 0)

    def test_rejects_invalid_baseline(self):
        for value in (0, -1, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                get_recommendations(value, 7, 5, 2)

    def test_rejects_invalid_tariff(self):
        for value in (-1, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                get_recommendations(520, value, 5, 2)

    def test_rejects_invalid_percentage(self):
        for value in (-1, 101, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                get_recommendations(520, 7, value, 2)

    def test_ranking_uses_savings_and_ease(self):
        items = [
            {"title": "Large but difficult", "estimated_money_saved": 100, "ease_score": 1},
            {"title": "Smaller and easy", "estimated_money_saved": 50, "ease_score": 5},
        ]
        ranked = rank_recommendations(items)
        self.assertEqual(ranked[0]["title"], "Smaller and easy")
        self.assertEqual(ranked[0]["priority"], "High")
        self.assertEqual(ranked[1]["priority"], "Medium")

    def test_zero_savings_are_low_priority(self):
        items = rank_recommendations([
            {"title": "No saving", "estimated_money_saved": 0, "ease_score": 4}
        ])
        self.assertEqual(items[0]["priority"], "Low")

    def test_ranking_does_not_mutate_original_items(self):
        original = [{"title": "A", "estimated_money_saved": 5, "ease_score": 3}]
        ranked = rank_recommendations(original)
        self.assertNotIn("rank", original[0])
        self.assertIn("rank", ranked[0])


if __name__ == "__main__":
    unittest.main()
