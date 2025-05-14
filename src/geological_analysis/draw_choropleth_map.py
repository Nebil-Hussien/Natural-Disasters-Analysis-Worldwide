"""
This module provides a function to draw a choropleth
map showing the number of specific disaster types by country.
"""


import plotly.express as px


def draw_choropleth_map(data, disaster_type, title, colorscale):
    """
    Draw a choropleth map showing the number of specific disaster types by
    country.

    Parameters:
    data (pd.DataFrame): DataFrame containing the disaster data.
    disaster_type (str): The type of disaster to filter by.
    title (str): The title of the map.
    colorscale (str or list): The colorscale for the choropleth map.
    """
    # Filter data for the specific disaster type
    filtered_data = data[data['Disaster Type'] == disaster_type]

    # Aggregate data by country
    disaster_counts = filtered_data.groupby('Country').size().reset_index(
        name='Counts'
    )

    # Create the choropleth map
    fig = px.choropleth(
        disaster_counts,
        locations='Country',
        locationmode='country names',
        color='Counts',
        hover_name='Country',
        color_continuous_scale=colorscale,
        title=title,
        labels={'Counts': 'Number of Disasters'}
    )

    # Show the map
    fig.show()


# Example usage
# draw_choropleth_map(data, 'Flood', 'Flood prone Country', 'Blues')
