"""
Unit tests for the compare_by_region function
in the compare_by_region module.
"""

import sys
import os
import unittest
import pandas as pd

# Ensure correct import path before importing compare_by_region
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..', '..',
            'src', 'administrative_responses'
        )
    )
)

from compare_by_region import compare_by_region  # pylint: disable=import-error


class TestCompareByRegion(unittest.TestCase):
    """
    Test case for the compare_by_region function.
    """

    def setUp(self):
        """
        Set up test data for compare_by_region function.
        """
        self.data = pd.DataFrame({
            'Region': ['A', 'B', 'C'],
            'Latitude': [0, 10, 20],
            'Longitude': [0, 10, 20],
            'Total Deaths': [100, 200, 150]
        })

    def test_compare_by_region(self):
        """
        Test the compare_by_region function with sample data.
        """
        try:
            compare_by_region(self.data)
        except Exception as exc:  # pylint: disable=broad-except
            self.fail(f"compare_by_region raised an exception: {exc}")


if __name__ == '__main__':
    unittest.main()
