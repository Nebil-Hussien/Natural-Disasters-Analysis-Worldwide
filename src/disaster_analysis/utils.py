"""
This module provides utility functions for disaster analysis.
"""

def check_required_columns(data_frame, required_columns):
    """
    Check if the required columns exist in the DataFrame.

    Parameters:
    data_frame: pd.DataFrame
        DataFrame containing the dataset with relevant columns.
    required_columns: list of str
        List of column names that are required in the DataFrame.

    Returns:
    bool
        True if all required columns are present, False otherwise.
    """
    missing_columns = [col for col in required_columns if col not in data_frame.columns]
    if missing_columns:
        print(f"Missing required columns: {', '.join(missing_columns)}")
        return False
    return True

