"""
This module provides functionality to perform t-tests for administrative
responses on Total Deaths and Total Affected, with results optionally
displayed or saved to a file.
"""

import argparse
import pandas as pd
from scipy.stats import ttest_ind


def t_test_response(data, responses=None):
    """
    Perform t-tests for administrative responses
    on Total Deaths and Total Affected.

    Parameters:
    - data (pd.DataFrame): The DataFrame to analyze.
    - responses (list, optional):
      List of response columns to analyze.

    Returns:
    - dict: A dictionary with t-test results.
    """
    if data is None:
        print("Error: No data provided for t-test analysis.")
        return {}

    if responses is None:
        responses = ['OFDA/BHA Response', 'Appeal', 'Declaration']

    results = {}
    try:
        for response in responses:
            with_response = data[data[response] == 'Yes']
            without_response = data[data[response] == 'No']

            if not with_response.empty and not without_response.empty:
                t_stat_deaths, p_val_deaths = ttest_ind(
                    with_response['Total Deaths'],
                    without_response['Total Deaths'],
                    equal_var=False
                )
                t_stat_affected, p_val_affected = ttest_ind(
                    with_response['Total Affected'],
                    without_response['Total Affected'],
                    equal_var=False
                )

                results[response] = {
                    'Total Deaths': (t_stat_deaths, p_val_deaths),
                    'Total Affected': (t_stat_affected, p_val_affected)
                }
            else:
                print(
                    f"Warning: Not enough data for {response} "
                    f"to perform t-test."
                )
    except KeyError as e:
        print(f"Error: Column not found in the data: {e}")
    except Exception as e:  # pylint: disable=broad-except
        print(f"An unexpected error occurred during t-test analysis: {e}")

    print(results)
    return results


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="T-Test Response Component")
    parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )
    parser.add_argument(
        '--responses', nargs='+', help="Responses to analyze"
    )
    return parser.parse_args()


def main():
    """Main function to run the t-test analysis."""
    args = parse_args()
    data = pd.read_excel(args.input)
    t_test_response(data, args.responses)


if __name__ == "__main__":
    main()
