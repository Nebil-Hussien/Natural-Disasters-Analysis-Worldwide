"""
This module provides functionality to plot the number of injuries and deaths over years
using data from an Excel file. It includes functions to load data, clean it,
and generate a line plot comparing the total number of injured and deceased individuals over the years.
"""

import argparse
import os
import matplotlib.pyplot as plt

from src.helper_functions import load_data, clean_data
from src.disaster_analysis.utils import check_required_columns

def plot_injured_and_deaths_over_years(data_frame, output_dir):
    """
    Plot the number of injured and deaths over years using Matplotlib and save the plot as a PNG.

    Parameters:
    data_frame: pd.DataFrame
        DataFrame containing the EMDAT dataset with relevant columns.
    output_dir: str
        Directory where the plot should be saved.
    """
    required_columns_injured = ['Start Year', 'No. Injured']
    if not check_required_columns(data_frame, required_columns_injured):
        return

    required_columns_deaths = ['Start Year', 'Total Deaths']
    if not check_required_columns(data_frame, required_columns_deaths):
        return

    injured_data = data_frame.groupby('Start Year')['No. Injured'].sum().reset_index()
    deaths_data = data_frame.groupby('Start Year')['Total Deaths'].sum().reset_index()

    # Plotting using Matplotlib
    plt.figure(figsize=(10, 6))

    plt.plot(injured_data['Start Year'], injured_data['No. Injured'],
             marker='o', linestyle='-', color='skyblue', label='Total Injured')
    plt.plot(deaths_data['Start Year'], deaths_data['Total Deaths'],
             marker='o', linestyle='-', color='salmon', label='Total Deaths')

    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Comparison of Injuries and Deaths Over Years')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, 'injuries_and_deaths_over_years.png')
    plt.savefig(output_path)  # Save the plot as an image
    plt.show()

    print("\nInjuries and Deaths Over Years:")
    print("Injuries:")
    print(injured_data.to_string(index=False))
    print("\nDeaths:")
    print(deaths_data.to_string(index=False))

def parse_args():
    """
    Parse command-line arguments for the script.

    Returns:
    argparse.Namespace
        The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Plot Injuries and Deaths Over Years")
    parser.add_argument('--input', type=str, required=True, help="Input Excel file path")
    parser.add_argument('--output_dir', type=str, default='results',
                        help="Directory for saving the plot")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    data_frame = load_data(args.input)
    cleaned_data = clean_data(data_frame)
    plot_injured_and_deaths_over_years(cleaned_data, args.output_dir)

