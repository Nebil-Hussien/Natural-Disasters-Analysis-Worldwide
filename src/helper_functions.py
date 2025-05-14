"""
This module provides functions to load, preprocess, and clean data
from an Excel file, specifically for disaster-related datasets.
"""

import argparse
import os
import pandas as pd


def load_data(file_path):
    """
    Load data from an Excel file.

    Parameters:
    - file_path (str): The path to the Excel file.

    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame,
    or None if an error occurs.
    """
    try:
        data = pd.read_excel(file_path, index_col=0)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except ValueError:
        print("Error: The file is not in the expected Excel format (XLSX).")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"An unexpected error occurred: {e}")
        return None


def data_preprocessing(input_path, output_path=None):
    """
    Pre-process the data and optionally
    save a clean DataFrame for further processing.

    Parameters:
    - input_path (str): The path to the input Excel file.
    - output_path (str, optional): The path to save the cleaned Excel file.

    Returns:
    - pd.DataFrame: The pre-processed DataFrame, or None if an error occurs.
    """
    print(f"Loading data from {input_path}")  # Debugging print statement
    data = load_data(input_path)
    if data is None:
        return None

    try:
        data.drop(
            [
                "AID Contribution ('000 US$)",
                "Reconstruction Costs ('000 US$)",
                "Reconstruction Costs, Adjusted ('000 US$)",
                "Insured Damage ('000 US$)",
                "Insured Damage, Adjusted ('000 US$)"
            ],
            axis="columns",
            inplace=True
        )
        data['Start Year'] = data['Start Year'].astype(int)
        data['End Year'] = data['End Year'].astype(int)
        data['Total Deaths'] = data['Total Deaths'].fillna(0).astype(int)
        data["Total Damage, Adjusted ('000 US$)"] = data[
            "Total Damage, Adjusted ('000 US$)"
        ].fillna(0).astype(float)

        if output_path:
            # Ensure the 'results' directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            data.to_excel(output_path, index=False)
        return data

    except KeyError as e:
        print(f"Error: One or more columns to drop "
              f"do not exist in the data: {e}")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"An unexpected error occurred during data preprocessing: {e}")
        return None


def clean_data(data):
    """
    Clean the data by filling missing values and converting data types.

    Parameters:
    - data (pd.DataFrame): The DataFrame to clean.

    Returns:
    - pd.DataFrame: The cleaned DataFrame, or None if an error occurs.
    """
    if data is None:
        print("Error: No data provided for cleaning.")
        return None

    try:
        # Fill missing values
        data['Total Deaths'] = data['Total Deaths'].fillna(0)
        data['Total Affected'] = data['Total Affected'].fillna(0)

        # Convert categorical columns to 'category' type
        categorical_columns = [
            'Region', 'Disaster Type', 'OFDA/BHA Response',
            'Appeal', 'Declaration'
        ]
        for col in categorical_columns:
            data[col] = data[col].astype('category')

        return data

    except KeyError as e:
        print(f"Error: Column not found in the data: {e}")
        return None
    except Exception as e:  # pylint: disable=broad-except
        print(f"An unexpected error occurred during data cleaning: {e}")
        return None


def main():
    """Main function to run CLI commands."""
    parser = argparse.ArgumentParser(description="Data Processing CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for loading data
    load_parser = subparsers.add_parser(
        'load', help="Load data from an Excel file"
    )
    load_parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )

    # Subparser for data preprocessing
    preprocess_parser = subparsers.add_parser(
        'preprocess', help="Preprocess the data"
    )
    preprocess_parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )
    preprocess_parser.add_argument(
        '--output', type=str, help="Output Excel file path",
        default='../results/preprocessed_data.xlsx'
    )

    # Subparser for cleaning data
    clean_parser = subparsers.add_parser(
        'clean', help="Clean the data"
    )
    clean_parser.add_argument(
        '--input', type=str, required=True, help="Input Excel file path"
    )
    clean_parser.add_argument(
        '--output', type=str, help="Output Excel file path",
        default='../results/cleaned_data.xlsx'
    )

    args = parser.parse_args()

    if args.command == 'load':
        data = load_data(args.input)
        if data is not None:
            print("Data loaded successfully!")
            print(data.head())
        else:
            print("Failed to load data.")

    elif args.command == 'preprocess':
        data = data_preprocessing(args.input, args.output)
        if data is not None:
            print(f"Data preprocessed successfully "
                  f"and saved to {args.output}!")
            print(data.head())
        else:
            print("Data preprocessing failed.")

    elif args.command == 'clean':
        data = load_data(args.input)
        if data is not None:
            cleaned_data = clean_data(data)
            if cleaned_data is not None:
                # Ensure the 'results' directory exists
                os.makedirs(os.path.dirname(args.output), exist_ok=True)
                cleaned_data.to_excel(args.output, index=False)
                print(f"Data cleaned successfully and saved to {args.output}!")
                print(cleaned_data.head())
            else:
                print("Data cleaning failed.")
        else:
            print("Failed to load data for cleaning.")


if __name__ == "__main__":
    main()
