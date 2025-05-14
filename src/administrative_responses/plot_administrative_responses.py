"""
This module provides functionality to plot Total Deaths and Total Affected
by administrative responses, with the option to save the plots as PNG files.
"""

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# pylint: disable=redefined-outer-name
def plot_administrative_responses(data, output_prefix=None):
    """
    Plot Total Deaths and Total Affected by administrative responses
    and optionally save as PNG files.

    Parameters:
    - data (pd.DataFrame): The data to plot.
    - output_prefix (str, optional): The prefix for the output file names.
      If None, plots are displayed instead.
    """
    try:
        responses = ['OFDA/BHA Response', 'Appeal', 'Declaration']

        # Check if required columns are present in the data
        required_columns = responses + ['Total Deaths', 'Total Affected']
        for col in required_columns:
            if col not in data.columns:
                raise KeyError(
                    f"Required column '{col}' not found in data."
                )

        # Define thresholds to filter extreme outliers
        death_threshold = data['Total Deaths'].quantile(0.95)
        affected_threshold = data['Total Affected'].quantile(0.95)

        # Filter data to exclude extreme outliers
        filtered_data = data[
            (data['Total Deaths'] <= death_threshold) &
            (data['Total Affected'] <= affected_threshold)
        ]

        for response in responses:
            plt.figure(figsize=(14, 6))

            # Plot Total Deaths by response with a linear scale
            plt.subplot(1, 2, 1)
            sns.boxplot(x=response, y='Total Deaths', data=filtered_data)
            plt.title(f'Total Deaths by {response}')
            # Use linear scale for better visibility
            plt.yscale('linear')

            # Plot Total Affected by response with a linear scale
            plt.subplot(1, 2, 2)
            sns.boxplot(x=response, y='Total Affected', data=filtered_data)
            plt.title(f'Total Affected by {response}')
            # Use linear scale for better visibility
            plt.yscale('linear')

            plt.tight_layout()

            if output_prefix:
                # Save the figure as a PNG file
                output_file = (
                    f"{output_prefix}_{response.replace('/', '_')}.png"
                )
                plt.savefig(output_file)
                plt.close()
                print(f"Plot saved as {output_file}")
            else:
                # Display the plot
                plt.show()

    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:  # pylint: disable=broad-except
        print(
            f"An unexpected error occurred while plotting administrative "
            f"responses: {e}"
        )


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Plot Administrative Responses Component"
    )
    parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )
    parser.add_argument(
        '--output_prefix', type=str,
        help="Output file prefix for the PNG files (optional)"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    data = pd.read_excel(args.input)
    plot_administrative_responses(data, args.output_prefix)
