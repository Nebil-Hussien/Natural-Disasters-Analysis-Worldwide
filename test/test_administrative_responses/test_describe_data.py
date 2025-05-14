"""
Unit tests for the describe_data function
in the describe_data module.
"""

import sys
import os
import unittest
import pandas as pd

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

# pylint: disable=import-error
from describe_data import describe_data


class TestDescribeData(unittest.TestCase):
    """
    Test case for the describe_data function.
    """

    def setUp(self):
        """
        Set up test data for describe_data function.
        """
        self.data = pd.DataFrame({
            'Total Deaths': [1, 2, 3],
            'Total Affected': [10, 20, 30],
            'Region': ['A', 'B', 'C'],
            'Disaster Type': ['X', 'Y', 'Z']
        })

    def test_describe_data(self):
        """
        Test the describe_data function with sample data.
        """
        try:
            describe_data(self.data)
        except Exception as exc:  # pylint: disable=broad-except
            self.fail(f"describe_data raised an exception: {exc}")


if __name__ == '__main__':
    unittest.main()
