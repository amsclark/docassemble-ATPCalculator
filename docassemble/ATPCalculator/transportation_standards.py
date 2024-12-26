import pandas as pd
from docassemble.base.util import path_and_mimetype

def get_transportation_standards():
  try:
    transport_filename = f"data/sources/transportationstandards.csv"
    the_csv_file, csv_file_mimetype = path_and_mimetype(transport_filename)
    with open(the_csv_file, "r") as f:
      transportation_standards = pd.read_csv(f)
    return transportation_standards
  except FileNotFoundError:
    return "File Not Found"
  except pd.errors.EmptyDataError:
    return "The file is empty"
  except Exception as e:
    return e
    