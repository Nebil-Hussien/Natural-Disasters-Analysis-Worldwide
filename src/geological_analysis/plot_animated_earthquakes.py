"""
This module provides a function to plot an animated
geographical scatter plot of earthquakes
with magnitude 6.5 or greater over the past 20 years.
"""


import datetime
import pandas as pd
import plotly.express as px


def plot_animated_earthquakes(data):
    """
    Plot an animated geographical scatter plot of earthquakes
    with magnitude 6.5 or greater over the past 20 years.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the disaster data.
    """
    # Convert 'Start Year' to datetime and filter for the last 20 years
    current_year = datetime.datetime.now().year
    data['Start Year'] = pd.to_datetime(data['Start Year'], format='%Y')
    filtered_data = data.loc[
        (data['Disaster Type'] == 'Earthquake') &
        (data['Start Year'].dt.year >= (current_year - 20)) &
        (data['Magnitude'] >= 6.5)
    ]

    # Prepare the data for the animated map
    timeline_data = filtered_data[[
        'Start Year', 'Country', 'Region', 'Magnitude',
        'Latitude', 'Longitude'
    ]].copy()
    timeline_data['Year'] = timeline_data['Start Year'].dt.year
    timeline_data = timeline_data.sort_values(by='Start Year')

    # Create the animated geographical scatter plot
    fig = px.scatter_geo(
        timeline_data,
        lat='Latitude',
        lon='Longitude',
        color='Magnitude',
        hover_name='Country',
        size='Magnitude',
        animation_frame='Year',
        projection='natural earth',
        title='Animated Timeline of Earthquakes (M6.5+) '
        'Over the Past 20 Years',
        template='plotly_white'
    )

    # Customize the layout for better readability
    fig.update_layout(
        geo={
            'showland': True,
            'landcolor': 'rgb(243, 243, 243)',
            'subunitcolor': 'rgb(217, 217, 217)',
            'countrycolor': 'rgb(217, 217, 217)'
        },
        title_x=0.5
    )

    # Show the plot
    fig.show()

# Example usage
# plot_animated_earthquakes(data)
