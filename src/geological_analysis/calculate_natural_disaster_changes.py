"""
This module provides a function to calculate the changes
in frequency of natural disaster types
over the past specified number of years.
"""

import datetime
import pandas as pd


def calculate_natural_disaster_changes(data, years_past):
    """
    Calculate the changes in frequency of natural disaster types over
    the past specified number of years.

    Parameters:
    - data: DataFrame containing the disaster data.
    - years_past: Number of years in the past to compare with
    the most recent years.

    Returns:
    - changes_df: DataFrame showing the increase or decrease in frequency of
    each natural disaster type.
    """
    try:
        # Convert 'Start Year' to datetime and create a 'Year' column
        data = data.copy()  # Use a copy to avoid modifying the original data
        data['Start Year'] = pd.to_datetime(data['Start Year'], format='%Y')
        data['Year'] = data['Start Year'].dt.year

        current_year = datetime.datetime.now().year
        past_year = current_year - years_past

        # Filter data for natural disasters
        natural_disasters = data[data['Disaster Group'] == 'Natural']

        # Filter data for the past and recent years
        past_data = natural_disasters[natural_disasters['Year'] < past_year]
        recent_data = natural_disasters[natural_disasters['Year'] >= past_year]

        # Initialize a dictionary to hold the results
        changes = {
            'Disaster Type': [],
            'Past Frequency': [],
            'Recent Frequency': [],
            'Change': []
        }

        disaster_types = natural_disasters['Disaster Type'].unique()

        for disaster_type in disaster_types:
            # Calculate the average frequency per year for
            # past and recent periods
            past_frequency = (
                past_data[past_data['Disaster Type'] == disaster_type]
                .shape[0] / years_past
            )
            recent_frequency = (
                recent_data[recent_data['Disaster Type'] == disaster_type]
                .shape[0] / years_past
            )

            # Calculate the change
            change = recent_frequency - past_frequency

            # Append results to the dictionary
            changes['Disaster Type'].append(disaster_type)
            changes['Past Frequency'].append(past_frequency)
            changes['Recent Frequency'].append(recent_frequency)
            changes['Change'].append(change)

        # Convert the dictionary to a DataFrame
        changes_df = pd.DataFrame(changes)
        return changes_df

    except KeyError as error:
        print(f"KeyError occurred: {error}")
        return None
    except ValueError as error:
        print(f"ValueError occurred: {error}")
        return None
    except TypeError as error:
        print(f"TypeError occurred: {error}")
        return None
    except AttributeError as error:
        print(f"AttributeError occurred: {error}")
        return None
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None

# Example usage
# changes_df = calculate_natural_disaster_changes(data, 20)
# print(changes_df)
