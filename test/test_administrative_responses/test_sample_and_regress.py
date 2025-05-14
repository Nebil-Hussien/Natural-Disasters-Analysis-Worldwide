"""
Unit tests for the sample_and_regress function
in the sample_and_regress module.
"""

import sys
import os
import unittest
import pandas as pd

# Ensure correct import path before importing sample_and_regress
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

# Import the sample_and_regress function after setting the path
# pylint: disable=import-error
from sample_and_regress import sample_and_regress


class TestSampleAndRegress(unittest.TestCase):
    """
    Test case for the sample_and_regress function.
    """

    def setUp(self):
        """
        Set up test data for sample_and_regress function.
        """
        self.data = pd.DataFrame({
            'Total Deaths': [1, 2, 3],
            'Total Affected': [10, 20, 30],
            'Region': ['A', 'B', 'C'],
            'Disaster Type': ['X', 'Y', 'Z'],
            'OFDA/BHA Response': ['Yes', 'No', 'Yes'],
            'Appeal': ['No', 'Yes', 'No'],
            'Declaration': ['Yes', 'No', 'Yes']
        })
        self.selected_features = [
            'Total Affected', 'Region', 'Disaster Type',
            'OFDA/BHA Response', 'Appeal', 'Declaration'
        ]

    def test_sample_and_regress(self):
        """
        Test the sample_and_regress function with sample data.
        """
        model = sample_and_regress(self.data, self.selected_features)
        self.assertIsNotNone(model)
        self.assertIn('Total Affected', model.params)


if __name__ == '__main__':
    unittest.main()
