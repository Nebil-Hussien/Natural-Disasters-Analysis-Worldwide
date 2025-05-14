"""
This module provides functionality to perform a simplified regression analysis
using selected features and optionally save the regression summary to a file.
"""

import argparse
import pandas as pd
import statsmodels.api as sm


def sample_and_regress(
    data, selected_features=None, target_variable='Total Deaths',
    output_file=None
):
    """
    Perform a simplified regression analysis using selected features.

    Parameters:
    - data (pd.DataFrame): The DataFrame to analyze.
    - selected_features (list, optional):
      List of features to include in the model.
    - target_variable (str, optional):
      The target variable for the regression.
      Default is 'Total Deaths'.
    - output_file (str, optional):
      The path to save the regression summary.
      If None, results are printed.

    Returns:
    - sm.OLSResults: Fitted regression model.
    """
    if data is None or len(data) == 0:
        print("Error: No data provided or data is empty.")
        return None

    if selected_features is None:
        # Default features
        selected_features = ['OFDA/BHA Response', 'Region']

    try:
        # Prepare the data for regression with selected features
        x_data = data[selected_features]
        x_data = pd.get_dummies(x_data, drop_first=True).astype(int)
        # Convert to float
        x_data = x_data.astype(float)

        # Convert dependent variable to numeric and handle missing values
        y_data = pd.to_numeric(
            data[target_variable], errors='coerce'
        ).fillna(0).values

        # Add a constant term for the intercept
        x_data = sm.add_constant(x_data)

        # Fit the regression model for the target variable
        model = sm.OLS(y_data, x_data).fit()

        if output_file:
            # Save the regression summary to a text file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(model.summary().as_text())
            print(
                f"Simplified Regression Analysis results saved to "
                f"{output_file}"
            )
        else:
            print("Simplified Regression Analysis:")
            print(model.summary())

        return model

    except KeyError as e:
        print(f"Error: Column not found in the data: {e}")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"An unexpected error occurred during regression analysis: {e}")
        return None


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Sample and Regress Component"
    )
    parser.add_argument(
        '--input', type=str, required=True,
        help="Input Excel file path"
    )
    parser.add_argument(
        '--selected_features', nargs='+',
        help="Features to include in the model"
    )
    parser.add_argument(
        '--target_variable', type=str, default='Total Deaths',
        help="The target variable for the regression"
    )
    parser.add_argument(
        '--output', type=str,
        help="Output file path for the regression summary"
    )
    return parser.parse_args()


def main():
    """Main function to run the sample and regress process."""
    args = parse_args()
    data = pd.read_excel(args.input)
    if args.selected_features:
        selected_features = args.selected_features
    else:
        selected_features = ['OFDA/BHA Response', 'Region']
    sample_and_regress(
        data, selected_features, args.target_variable, args.output
    )


if __name__ == "__main__":
    main()
