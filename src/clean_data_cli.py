import pandas as pd
import argparse

def clean_data(data):
    """
    Clean the data by filling missing values and converting data types.

    Parameters:
    - data (pd.DataFrame): The DataFrame to clean.
    
    Returns:
    - pd.DataFrame: The cleaned DataFrame.
    """
    if data is None:
        print("Error: No data provided for cleaning.")
        return None
    
    try:
        # Fill missing values
        data['Total Deaths'] = data['Total Deaths'].fillna(0)
        data['Total Affected'] = data['Total Affected'].fillna(0)
        
        # Convert categorical columns to 'category' type
        categorical_columns = ['Region', 'Disaster Type', 'OFDA/BHA Response', 'Appeal', 'Declaration']
        for col in categorical_columns:
            data[col] = data[col].astype('category')
        
        return data
    except KeyError as e:
        print(f"Error: Column not found in the data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during data cleaning: {e}")
        return None
