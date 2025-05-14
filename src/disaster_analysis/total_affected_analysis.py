"""
This module provides functionality to plot total affected over years
using data from an Excel file. It includes functions to load data, clean it,
and generate a bar and scatter plot showing the total number of affected individuals over the years.
"""

import argparse
import os
import matplotlib.pyplot as plt

from src.helper_functions import load_data, clean_data
from src.disaster_analysis.utils import check_required_columns

def plot_total_affected_over_years(data_frame, output_dir):
    """
    Plot the total affected over years using Matplotlib and save the plot as a PNG.

    Parameters:
    data_frame: pd.DataFrame
        DataFrame containing the EMDAT dataset with relevant columns.
    output_dir: str
        Directory where the plot should be saved.
    """
    required_columns = ['Start Year', 'Total Affected']
    if not check_required_columns(data_frame, required_columns):
        return

    grouped_data = data_frame.groupby('Start Year')['Total Affected'].sum().reset_index()

    # Plotting using Matplotlib
    plt.figure(figsize=(10, 6))

    # Bar plot
    plt.bar(grouped_data['Start Year'], grouped_data['Total Affected'],
            color='skyblue', label='Total Affected')

    # Scatter plot (markers)
    plt.scatter(grouped_data['Start Year'], grouped_data['Total Affected'],
                c=grouped_data['Total Affected'], cmap='viridis', s=100, edgecolor='k',
                alpha=0.8, label='Total Affected Markers')

    plt.colorbar(label='Total Affected')

    plt.xlabel('Year')
    plt.ylabel('Total Affected')
    plt.title('Total Affected Over Years')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, 'total_affected_over_years.png')
    plt.savefig(output_path)  # Save the plot as an image
    plt.show()

    print("\nTotal Affected Over Years:")
    print(grouped_data.to_string(index=False))

def parse_args():
    """
    Parse command-line arguments for the script.

    Returns:
    argparse.Namespace
        The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Plot Total Affected Over Years")
    parser.add_argument('--input', type=str, required=True, help="Input Excel file path")
    parser.add_argument('--output_dir', type=str, default='results',
                        help="Directory for saving the plot")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    data_frame = load_data(args.input)
    cleaned_data = clean_data(data_frame)
    plot_total_affected_over_years(cleaned_data, args.output_dir)
