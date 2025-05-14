"""
This module provides functionality to plot total deaths by disaster type
using data from an Excel file. It includes functions to load data, clean it,
and generate a bar plot showing the total number of deaths by disaster type.
"""

import argparse
import os
import matplotlib.pyplot as plt
import numpy as np

from src.helper_functions import load_data, clean_data
from src.disaster_analysis.utils import check_required_columns

def plot_deaths_by_disaster_type(data_frame, output_dir):
    """
    Plot the total fatalities by disaster type using Matplotlib and save the plot as a PNG.

    Parameters:
    data_frame: pd.DataFrame
        DataFrame containing the EMDAT dataset with relevant columns.
    output_dir: str
        Directory where the plot should be saved.
    """
    required_columns = ['Disaster Type', 'Total Deaths']
    if not check_required_columns(data_frame, required_columns):
        return

    grouped_data = data_frame.groupby('Disaster Type', observed=True)['Total Deaths'].sum().reset_index()

    # Plotting using Matplotlib
    plt.figure(figsize=(12, 8))

    num_types = len(grouped_data)
    bar_width = 0.4
    x_positions = np.arange(num_types)

    plt.bar(x_positions, grouped_data['Total Deaths'], width=bar_width,
            color='lightcoral', label='Total Deaths')

    plt.xlabel('Disaster Type')
    plt.ylabel('Count')
    plt.title('Total Deaths by Disaster Type')
    plt.xticks(x_positions, grouped_data['Disaster Type'], rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, 'total_deaths_by_disaster_type.png')
    plt.savefig(output_path)  # Save the plot as an image
    plt.show()

    print("\nTotal Deaths by Disaster Type:")
    print(grouped_data.to_string(index=False))

def parse_args():
    """
    Parse command-line arguments for the script.

    Returns:
    argparse.Namespace
        The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Plot Total Deaths by Disaster Type")
    parser.add_argument('--input', type=str, required=True, help="Input Excel file path")
    parser.add_argument('--output_dir', type=str, default='results',
                        help="Directory for saving the plot")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    data_frame = load_data(args.input)
    cleaned_data = clean_data(data_frame)
    plot_deaths_by_disaster_type(cleaned_data, args.output_dir)

