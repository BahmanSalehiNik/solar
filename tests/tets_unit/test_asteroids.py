from unittest import TestCase
from src.conf import KILOMETER_TO_MILE_CONSTANT


class TestAsteroidDataCollector(TestCase):
    def test_unit_conversion(self):
        self.assertAlmostEqual(1.60934 * KILOMETER_TO_MILE_CONSTANT, 1, places=5)
