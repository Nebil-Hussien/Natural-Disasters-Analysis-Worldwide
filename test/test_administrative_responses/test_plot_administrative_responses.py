"""
Unit tests for the plot_administrative_responses function
in the plot_administrative_responses module.
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
from plot_administrative_responses import plot_administrative_responses


class TestPlotAdministrativeResponses(unittest.TestCase):
    """
    Test case for the plot_administrative_responses function.
    """

    def setUp(self):
        """
        Set up test data for plot_administrative_responses function.
        """
        self.data = pd.DataFrame({
            'OFDA/BHA Response': ['Yes', 'No', 'Yes'],
            'Appeal': ['No', 'Yes', 'No'],
            'Declaration': ['Yes', 'No', 'Yes'],
            'Total Deaths': [100, 200, 150],
            'Total Affected': [1000, 2000, 1500]
        })

    def test_plot_administrative_responses(self):
        """
        Test the plot_administrative_responses function with sample data.
        """
        try:
            plot_administrative_responses(self.data)
        except Exception as exc:  # pylint: disable=broad-except
            self.fail(
                f"plot_administrative_responses raised an exception: {exc}"
                )


if __name__ == '__main__':
    unittest.main()
