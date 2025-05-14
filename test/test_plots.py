import unittest
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from src.plotting_scripts import check_required_columns, plot_total_affected_over_years, plot_injured_and_deaths_over_years, plot_deaths_by_disaster_type

class TestPlottingScripts(unittest.TestCase):
    def setUp(self):
        # Create mock data for testing
        self.data = pd.DataFrame({
            'Start Year': np.arange(2000, 2010),
            'Total Affected': np.random.randint(1000, 10000, 10),
            'No. Injured': np.random.randint(100, 1000, 10),
            'Total Deaths': np.random.randint(10, 100, 10),
            'Disaster Type': ['Flood', 'Earthquake', 'Storm', 'Wildfire', 'Flood', 'Earthquake', 'Storm', 'Wildfire', 'Flood', 'Earthquake']
        })

    def test_check_required_columns(self):
        # Test with all required columns
        required_columns = ['Start Year', 'Total Affected']
        self.assertTrue(check_required_columns(self.data, required_columns))
        
        # Test with missing columns
        required_columns = ['Start Year', 'Missing Column']
        self.assertFalse(check_required_columns(self.data, required_columns))

    def test_plot_total_affected_over_years(self):
        # Test if the function runs without errors
        try:
            plot_total_affected_over_years(self.data)
        except Exception as e:
            self.fail(f"plot_total_affected_over_years raised an exception: {e}")

    def test_plot_injured_and_deaths_over_years(self):
        # Test if the function runs without errors
        try:
            plot_injured_and_deaths_over_years(self.data)
        except Exception as e:
            self.fail(f"plot_injured_and_deaths_over_years raised an exception: {e}")

    def test_plot_deaths_by_disaster_type(self):
        # Test if the function runs without errors
        try:
            plot_deaths_by_disaster_type(self.data)
        except Exception as e:
            self.fail(f"plot_deaths_by_disaster_type raised an exception: {e}")

    def tearDown(self):
        # Close all plots after each test
        plt.close('all')

if __name__ == '__main__':
    unittest.main()
