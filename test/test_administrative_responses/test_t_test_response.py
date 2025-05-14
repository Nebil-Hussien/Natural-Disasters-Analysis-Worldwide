"""
Unit tests for the t_test_response function in the t_test_response module.
"""

import sys
import os
import unittest
import pandas as pd

# Modify sys.path before importing the t_test_response module
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), '..', '..',
            'src', 'administrative_responses'
        )
    )
)

# Now import the t_test_response function
try:
    from t_test_response import t_test_response  # pylint: disable=import-error
except ImportError as exc:
    raise ImportError(
        "Failed to import t_test_response module. "
        "Ensure the path is set correctly."
    ) from exc


class TestTTestResponse(unittest.TestCase):
    """
    Test case for the t_test_response function.
    """

    def setUp(self):
        """
        Set up test data for t-test response function.
        """
        self.data = pd.DataFrame({
            'OFDA/BHA Response': ['Yes', 'No', 'Yes', 'No'],
            'Appeal': ['No', 'Yes', 'No', 'Yes'],
            'Declaration': ['Yes', 'No', 'Yes', 'No'],
            'Total Deaths': [100, 200, 150, 180],
            'Total Affected': [1000, 2000, 1500, 1700]
        })

    def test_t_test_response(self):
        """
        Test the t_test_response function with sample data.
        """
        results = t_test_response(self.data)
        self.assertIsInstance(results, dict)
        self.assertIn('OFDA/BHA Response', results)
        self.assertIn('Appeal', results)
        self.assertIn('Declaration', results)


if __name__ == '__main__':
    unittest.main()
