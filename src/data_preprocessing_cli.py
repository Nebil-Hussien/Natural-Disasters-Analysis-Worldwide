import sys
import os
import pandas as pd
import argparse

# Add src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from helper_functions import data_preprocessing

def parse_args():
    parser = argparse.ArgumentParser(description="Data Preprocessing Component")
    parser.add_argument('--input', type=str, required=True, help="Input Excel file path")
    parser.add_argument('--output', type=str, help="Output Excel file path")
    return parser.parse_args()

def main():
    args = parse_args()
    data_preprocessing(args.input, args.output)
    print("Data preprocessing complete.")

if __name__ == '__main__':
    main()
