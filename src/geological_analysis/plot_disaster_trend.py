"""
This module provides a function to plot
the trend of a specified disaster type over time.
"""


import pandas as pd
import matplotlib.pyplot as plt


def plot_disaster_trend(data, disaster_type):
    """
    Plot the trend of a specified disaster type over time.

    Parameters:
    - data: DataFrame containing the disaster data.
    - disaster_type: The type of disaster to analyze.
    """
    # Convert 'Start Year' to datetime
    data['Start Year'] = pd.to_datetime(data['Start Year'], format='%Y')
    data['Year'] = data['Start Year'].dt.year

    # Filter data for the specified disaster type
    filtered_data = data[data['Disaster Type'] == disaster_type]

    # Aggregate data by year
    disaster_counts = (
        filtered_data.groupby('Year').size().reset_index(name='Counts'))

    # Plot the trend
    plt.figure(figsize=(14, 8))
    plt.plot(disaster_counts['Year'],
             disaster_counts['Counts'], marker='o', linestyle='-')
    plt.xlabel('Year')
    plt.ylabel('Number of Disasters')
    plt.title(f'Trend of {disaster_type} Over Time')
    plt.grid(True)
    plt.show()
