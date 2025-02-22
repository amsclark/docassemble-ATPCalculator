min_penalty = 50
min_payment = 10
max_percent_payment = .10
max_num_monthly_payments = 36

#2023 Figures
# in household	Amount
#1	$14,580 
#2	$19,720 
#3	$24,860 
#4	$30,000 
#5	$35,140 
#6	$40,280 
#7	$45,420 
#8	$50,560 
# Add'l	 $5,140 
# Currently, the federal government publishes these as a table up to household size of 8, but if you work out the math it is always just a base number plus an increment amount multiplied by household size
poverty_base = 9440
poverty_increment = 5140

#IRS numbers circa April 24, 2023
food = {"1": 466, "2": 777, "3": 936, "4": 1123, "additional": 195.39}
housekeeping = {"1": 47, "2": 80, "3": 85, "4": 90, "additional": 16.16}
apparel_and_services = {"1": 96, "2": 145, "3": 207, "4": 252, "additional": 52.99}
personal_care = {"1": 43, "2": 78, "3": 91, "4": 97, "additional": 18.21}
miscellaneous = {"1": 189, "2": 309, "3": 381, "4": 431, "additional": 73.25}
# The IRS really does think that housekeeping and personal care costs go down when a third person is added to a household, and then costs go back up again when the fourth is added.
# November 2023 update: apparently not anymore?

def get_food_personal_care(care_dict, household_size):
  if household_size <= 4:
    return care_dict[str(household_size)]
  else:
    return care_dict["4"] + (care_dict["additional"] * (household_size - 4))

car_ownership = {"0": 0, "1": 629, "2": 1258}
car_operating = {"0": 0, "1": 225, "2": 450}
public_transport_allowance = 218

#household_size_options = {
#"one": "1",
#"two": "2",
#"three": "3",
#"four": "4",
#"five_or_more": "5+"
#}

number_cars_options = {"0":"0", "1":"1", "2":"2+"}

oop_65_or_older_allowance = {"under": 83, "sixty_five_or_older": 158}
def get_oop_allowance(num_65_older, num_under_65):
  return (num_65_older * oop_65_or_older_allowance['sixty_five_or_older']) + (num_under_65 * oop_65_or_older_allowance['under'])
  
FICA_rate = .0765

oi_labels = {
"inc_SS": "SSI/SSD/SS Retirement", 
"inc_unemp": "Unemployment", 
"inc_VA": "VA Benefits", 
"inc_tanf": "TANF", 
"inc_pens": "Pension", 
"inc_snap": "SNAP", 
"inc_alim": "Alimony", 
"inc_invest": "Investment / Int. / Rent", 
"inc_other_other": "Other Income",
"inc_oi_total": 0
}

states_dict = {
    "alabama": "Alabama",
    "alaska": "Alaska",
    "arizona": "Arizona",
    "arkansas": "Arkansas",
    "california": "California",
    "colorado": "Colorado",
    "connecticut": "Connecticut",
    "delaware": "Delaware",
    "florida": "Florida",
    "georgia": "Georgia",
    "hawaii": "Hawaii",
    "idaho": "Idaho",
    "illinois": "Illinois",
    "indiana": "Indiana",
    "iowa": "Iowa",
    "kansas": "Kansas",
    "kentucky": "Kentucky",
    "louisiana": "Louisiana",
    "maine": "Maine",
    "maryland": "Maryland",
    "massachusetts": "Massachusetts",
    "michigan": "Michigan",
    "minnesota": "Minnesota",
    "mississippi": "Mississippi",
    "missouri": "Missouri",
    "montana": "Montana",
    "nebraska": "Nebraska",
    "nevada": "Nevada",
    "new-hampshire": "New Hampshire",
    "new-jersey": "New Jersey",
    "new-mexico": "New Mexico",
    "new-york": "New York",
    "north-carolina": "North Carolina",
    "north-dakota": "North Dakota",
    "ohio": "Ohio",
    "oklahoma": "Oklahoma",
    "oregon": "Oregon",
    "pennsylvania": "Pennsylvania",
    "rhode-island": "Rhode Island",
    "south-carolina": "South Carolina",
    "south-dakota": "South Dakota",
    "tennessee": "Tennessee",
    "texas": "Texas",
    "utah": "Utah",
    "vermont": "Vermont",
    "virginia": "Virginia",
    "washington": "Washington",
    "west-virginia": "West Virginia",
    "wisconsin": "Wisconsin",
    "wyoming": "Wyoming",
    "district-of-columbia": "District of Columbia",
    "puerto-rico": "Puerto Rico"
}

tanf_alt_names = {
    "alabama": "Family Assistance Program",
    "alaska": "ATAP",
    "arizona": "Cash Assistance",
    "arkansas": "TEA",
    "california": "CalWORKs",
    "colorado": "Colorado Works",
    "connecticut": "TFA",
    "florida": "Temporary Cash Assistance",
    "iowa": "FIP",
    "kentucky": "KTAP",
    "louisiana": "FITAP",
    "massachusetts": "TAFDC",
    "michigan": "FIP",
    "minnesota": "MFIP",
    "missouri": "Temporary Assistance",
    "nebraska": "ADC",
    "new-hampshire": "FANF",
    "new-jersey": "WFNJ",
    "new-mexico": "New Mexico Works",
    "new-york": "Temporary Assistance",
    "north-carolina": "Work First",
    "ohio": "OWF",
    "rhode-island": "Rhode Island Works",
    "tennessee": "Families First",
    "utah": "FEP",
    "vermont": "Reach Up",
    "virginia": "Virginia Initiative for Employment Not Welfare",
    "west-virginia": "West Virginia Works",
    "wisconsin": "W-2",
    "wyoming": "POWER"
}