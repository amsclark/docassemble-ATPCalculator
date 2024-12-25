import pandas
from docassemble.base.util import path_and_mimetype

__all__ = ['get_county_names', 'county_info', 'get_total_housing_allowance', 'get_state_county_names', 'state_county_info', 'get_state_total_housing_allowance']

county_info_by_name = {}
county_names = []

def get_total_housing_allowance(county, household_size):
    if county not in county_info_by_name:
        raise Exception("Reference to invalid county " + county)
    if household_size <= 4:
        return clean_and_convert(county_info(county)[str(household_size)])
    else:
        return clean_and_convert(county_info(county)["five_or_more"])

def get_county_names():
    return county_names

def county_info(county):
    if county not in county_info_by_name:
        raise Exception("Reference to invalid county " + county)
    return county_info_by_name[county]

def read_state_data(state_name):
    filename = f"data/sources/{state_name}.tsv"
    the_tsv_file, mimetype = path_and_mimetype(filename)
    df = pandas.read_csv(the_tsv_file, sep='\t')
    state_county_info = {}
    state_county_names = []
    
    # Map the actual column names to shorter keys
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
    
    # Populate the global county_info_by_name with data from the current state's TSV
    global county_info_by_name
    county_info_by_name = state_county_info
    return state_county_info, state_county_names

def get_state_county_names(state_name):
    _, state_county_names = read_state_data(state_name)
    return state_county_names

def state_county_info(state_name, county):
    state_county_info, _ = read_state_data(state_name)
    if county not in state_county_info:
        raise Exception(f"Reference to invalid county {county} in state {state_name}")
    return state_county_info[county]

def get_state_total_housing_allowance(state_name, county, household_size):
    state_county_info, _ = read_state_data(state_name)
    if county not in state_county_info:
        raise Exception(f"Reference to invalid county {county} in state {state_name}")
    if household_size <= 4:
        return clean_and_convert(state_county_info[county][str(household_size)])
    else:
        return clean_and_convert(state_county_info[county]["five_or_more"])

def clean_and_convert(value):
    # Remove non-numeric characters (like $ and commas) and convert to float
    if isinstance(value, str):
        return float(value.replace('$', '').replace(',', ''))
    return float(value)
