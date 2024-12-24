import pandas
from docassemble.base.util import path_and_mimetype

__all__ = ['get_county_names', 'county_info', 'get_total_housing_allowance', 'read_state_data']

county_info_by_name = {}
county_names = []

def get_total_housing_allowance(county, household_size):
  if county not in county_info_by_name:
    raise Exception("Reference to invalid county " + county)
  if household_size <= 4:
    return county_info(county)[str(household_size)]
  else:
    return county_info(county)["five_or_more"]


def read_data(filename):
    the_xlsx_file, mimetype = path_and_mimetype(filename)
    df = pandas.read_excel(the_xlsx_file)
    for indexno in df.index:
        if not df['County'][indexno]:
            continue
        county_names.append(df['County'][indexno])
        county_info_by_name[df['County'][indexno]] = {"1": df['One'][indexno], "2": df['Two'][indexno], "3": df['Three'][indexno], "4": df['Four'][indexno], "five_or_more": df['Five_Or_More'][indexno]}

def get_county_names():
    return county_names

def county_info(county):
    if county not in county_info_by_name:
        raise Exception("Reference to invalid county " + county)
    return county_info_by_name[county]

def read_state_data(state_name):
    """
    Reads a .tsv file named after the given state and returns its contents as a DataFrame
    """
    filename = f"data/sources/{state_name}.tsv"
    the_tsv_file, mimetype = path_and_mimetype(filename)
    df = pandas.read_csv(the_tsv_file, sep='\t')
    
    # Process the DataFrame to match the structure of `read_data`
    state_county_info = {}
    state_county_names = []
    
    for indexno in df.index:
        if not df['County'][indexno]:
            continue
        state_county_names.append(df['County'][indexno])
        state_county_info[df['County'][indexno]] = {
            "1": df['2024 Published ALE Housing Expense for a Family of 1'][indexno],
            "2": df['2024 Published ALE Housing Expense for a Family of 2'][indexno],
            "3": df['2024 Published ALE Housing Expense for a Family of 3'][indexno],
            "4": df['2024 Published ALE Housing Expense for a Family of 4'][indexno],
            "five_or_more": df['2024 Published ALE Housing Expense for a Family of 5'][indexno]
        }

    return state_county_names, state_county_info
