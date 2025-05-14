"""
This module provides functionality to describe a dataset by
printing descriptive statistics and frequency counts for
specified categorical variables.
"""

import argparse
import pandas as pd


def describe_data(data):  # pylint: disable=redefined-outer-name
    """
    Print descriptive statistics and value counts for categorical variables.

    Parameters:
    - data (pd.DataFrame): The DataFrame to describe.
    """
    if data is None:
        print("Error: No data provided for description.")
        return

    try:
        print("Descriptive Statistics:")
        print(data[['Total Deaths', 'Total Affected']].describe())
        print("\nFrequency Counts:")
        for col in ['Region', 'Disaster Type']:
            print(f"{col}:")
            print(data[col].value_counts())
            print()
    except KeyError as e:
        print(f"Error: Column not found in the data: {e}")
    except Exception as e:  # pylint: disable=broad-except
        print(f"An unexpected error occurred during data description: {e}")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Describe Data Component")
    parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    data = pd.read_excel(args.input)
    describe_data(data)
