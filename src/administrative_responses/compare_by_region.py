"""
Module to compare deaths by region using a 3D Earth map visualization.
"""

import argparse
import pandas as pd
import plotly.graph_objects as go


# pylint: disable=redefined-outer-name
def compare_by_region(data, output_file=None):
    """
    Plot deaths on a 3D Earth map by region and optionally save the plot.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing 'Region',
      'Latitude', 'Longitude', and 'Total Deaths' columns.
    - output_file (str, optional): The path to save the output plot.
      If None, the plot is displayed.
    """
    if data is None:
        print("Error: No data provided for plotting.")
        return

    subsets = {'Region', 'Latitude', 'Longitude', 'Total Deaths'}
    if not subsets.issubset(data.columns):
        print(
            "Error: Data does not have the required columns 'Region', "
            "'Latitude', 'Longitude', and 'Total Deaths'."
        )
        return

    try:
        # Drop rows with NaN values in 'Total Deaths'
        data = data.dropna(subset=['Total Deaths'])

        # Create a scatter geo plot
        fig = go.Figure()

        # Add traces for each region
        for _, row in data.iterrows():
            death_ratio = row['Total Deaths'] / data['Total Deaths'].max()
            fig.add_trace(go.Scattergeo(
                lon=[row['Longitude']],
                lat=[row['Latitude']],
                text=f"{row['Region']}: {row['Total Deaths']} deaths",
                marker={
                    # Ensure size is at least 1
                    "size": max(1, death_ratio * 50),
                    "color": 'red',
                    "line_color": 'rgb(40,40,40)',
                    "line_width": 0.5,
                    "sizemode": 'area'
                },
                name=row['Region']
            ))

        # Update the layout for the globe
        fig.update_layout(
            title='Total Deaths by Region on 3D Earth Map',
            geo={
                "showframe": False,
                "showcoastlines": True,
                "projection_type": 'orthographic',
                "landcolor": 'rgb(255, 100, 217)',
                "oceancolor": 'rgb(20, 20, 255)',
                "showcountries": True,
            }
        )

        if output_file:
            # Save the figure as a PNG file
            fig.write_image(output_file)
            print(f"Plot saved as {output_file}")
        else:
            # Display the plot
            fig.show()

    except (KeyError, ValueError) as e:
        print(f"An error occurred during plotting: {e}")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Compare by Region Component")
    parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )
    parser.add_argument(
        '--output', type=str, help="Output file path for the plot (optional)"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    data = pd.read_excel(args.input)
    compare_by_region(data, args.output)
