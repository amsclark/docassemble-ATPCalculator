import pandas as pd
from docassemble.base.util import path_and_mimetype

def get_transportation_standards():
    filename = f"data/sources/Transportation_Standards.csv"
    try:
        # Read the CSV file
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found in the current directory.")
        return "FNF"
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filename}' is empty.")
        return "Empty"
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return e