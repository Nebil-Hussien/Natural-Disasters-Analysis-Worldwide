"""
Unit tests for the helper functions in the src.helper_functions module.
"""

import unittest
from unittest.mock import patch
import os
import pandas as pd
from src.helper_functions import load_data, data_preprocessing, clean_data


class TestHelperFunctions(unittest.TestCase):
    """
    Test case for the helper functions.
    """

    def setUp(self):
        """
        Set up the DataFrame to use in the tests.
        """
        self.test_data = pd.DataFrame({
            'Region': ['Region1', 'Region2'],
            'Disaster Type': ['Type1', 'Type2'],
            'OFDA/BHA Response': ['Yes', 'No'],
            'Appeal': ['Yes', 'No'],
            'Declaration': ['Yes', 'No'],
            'Total Deaths': [100, 200],
            'Total Affected': [1000, 2000],
            "Total Damage, Adjusted ('000 US$)": [500, 1000],
            "AID Contribution ('000 US$)": [150, 250],
            "Reconstruction Costs ('000 US$)": [300, 400],
            "Reconstruction Costs, Adjusted ('000 US$)": [350, 450],
            "Insured Damage ('000 US$)": [500, 600],
            "Insured Damage, Adjusted ('000 US$)": [550, 650],
            'Start Year': [2020, 2021],
            'End Year': [2021, 2022]
        })

        # Paths
        self.input_file_path = 'test_data.xlsx'
        self.output_file_path = '../results/test_output.xlsx'

    @patch('src.helper_functions.pd.read_excel')
    def test_load_data_success(self, mock_read_excel):
        """
        Test that data loads successfully from an Excel file.
        """
        mock_read_excel.return_value = self.test_data
        result = load_data(self.input_file_path)
        mock_read_excel.assert_called_once_with(
            self.input_file_path, index_col=0
        )
        pd.testing.assert_frame_equal(result, self.test_data)

    @patch('src.helper_functions.pd.read_excel')
    def test_load_data_file_not_found(self, mock_read_excel):
        """
        Test handling of FileNotFoundError in load_data.
        """
        mock_read_excel.side_effect = FileNotFoundError
        result = load_data(self.input_file_path)
        self.assertIsNone(result)

    @patch('src.helper_functions.pd.read_excel')
    def test_load_data_value_error(self, mock_read_excel):
        """
        Test handling of ValueError in load_data.
        """
        mock_read_excel.side_effect = ValueError
        result = load_data(self.input_file_path)
        self.assertIsNone(result)

    @patch('src.helper_functions.pd.read_excel')
    @patch('src.helper_functions.os.makedirs')
    @patch('src.helper_functions.pd.DataFrame.to_excel')
    def test_data_preprocessing_success(
        self, mock_to_excel, mock_makedirs, mock_read_excel
    ):
        """
        Test that data preprocessing works
        and saves the output file.
        """
        mock_read_excel.return_value = self.test_data

        result = data_preprocessing(
            self.input_file_path, self.output_file_path
        )

        self.assertIsNotNone(result)
        mock_read_excel.assert_called_once_with(
            self.input_file_path, index_col=0
        )
        self.assertNotIn("AID Contribution ('000 US$)", result.columns)
        self.assertNotIn("Reconstruction Costs ('000 US$)", result.columns)
        mock_makedirs.assert_called_once_with(
            os.path.dirname(self.output_file_path), exist_ok=True
        )
        mock_to_excel.assert_called_once_with(
            self.output_file_path, index=False)

    @patch('src.helper_functions.pd.read_excel')
    @patch('src.helper_functions.pd.DataFrame.to_excel')
    # pylint: disable=unused-argument
    def test_data_preprocessing_key_error(
        self, mock_to_excel, mock_read_excel
    ):
        """
        Test data preprocessing handles KeyError when columns are missing.
        """
        modified_data = self.test_data.drop(
            columns=["Total Damage, Adjusted ('000 US$)"]
        )
        mock_read_excel.return_value = modified_data

        result = data_preprocessing(
            self.input_file_path, self.output_file_path
        )
        self.assertIsNone(result)

    @patch('src.helper_functions.pd.read_excel')
    def test_clean_data_success(self, mock_read_excel):
        """
        Test that clean_data fills missing values
        and converts columns to categorical.
        """
        mock_read_excel.return_value = self.test_data

        result = clean_data(self.test_data)

        self.assertEqual(result['Total Deaths'].isnull().sum(), 0)
        self.assertEqual(result['Total Affected'].isnull().sum(), 0)
        self.assertTrue(
            isinstance(result['Region'].dtype, pd.CategoricalDtype)
        )
        self.assertTrue(
            isinstance(result['Disaster Type'].dtype, pd.CategoricalDtype)
        )

    @patch('src.helper_functions.pd.read_excel')
    def test_clean_data_key_error(self, mock_read_excel):
        """
        Test clean_data handles KeyError when expected columns are missing.
        """
        modified_data = self.test_data.drop(columns=['Region'])
        mock_read_excel.return_value = modified_data

        result = clean_data(modified_data)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
