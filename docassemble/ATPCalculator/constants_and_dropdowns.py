min_penalty = 50
min_payment = 1
max_percent_payment = .10
max_num_monthly_payments = 36

#2022 Figures
# in household	Amount
#1	$13,590 
#2	$18,310 
#3	$23,030 
#4	$27,750 
#5	$32,470 
#6	$37,190 
#7	$41,910 
#8	$46,630 
# Add'l	 $4,720 
# Currently, the federal government publishes these as a table up to household size of 8, but if you work out the math it is always just a base number plus an increment amount multiplied by household size
poverty_base = 8870
poverty_increment = 4720

food = {"1": 400, "2": 724, "3": 838, "4": 955, "additional": 187.16}
housekeeping = {"1": 41, "2": 76, "3": 69, "4": 79, "additional": 15.48}
apparel_and_services = {"1": 92, "2": 150, "3": 191, "4": 259, "additional": 50.76}
personal_care = {"1": 42, "2": 76, "3": 72, "4": 89, "additional": 17.44}
miscellaneous = {"1": 148, "2": 266, "3": 303, "4": 358, "additional": 70.16}
# The IRS really does think that housekeeping and personal care costs go down when a third person is added to a household, and then costs go back up again when the fourth is added.

def get_food_personal_care(care_dict, household_size):
  if household_size <= 4:
    return care_dict[str(household_size)]
  else:
    return care_dict["4"] + (care_dict["additional"] * (household_size - 4))

car_ownership = {"0": 0, "1": 533, "2": 1066}
car_operating = {"0": 0, "1": 201, "2": 402}
public_transport_allowance = 217

#household_size_options = {
#"one": "1",
#"two": "2",
#"three": "3",
#"four": "4",
#"five_or_more": "5+"
#}

number_cars_options = {"0":"0", "1":"1", "2":"2+"}

oop_65_or_older_allowance = {"under": 68, "sixty_five_or_older": 142}
def get_oop_allowance(sixty_five_or_older):
  if sixty_five_or_older:
    return oop_65_or_older_allowance['sixty_five_or_older']
  else:
    return oop_65_or_older_allowance['under']
  
FICA_rate = .0765

oi_labels = {
"inc_SS": "SSI/SSD/SS Retirement", 
"inc_unemp": "Unemployment", 
"inc_VA": "VA Benefits", 
"inc_tanf": "TANF/FIP", 
"inc_pens": "Pension", 
"inc_snap": "SNAP", 
"inc_alim": "Alimony", 
"inc_invest": "Investment / Int. / Rent", 
"inc_oi_total": 0
}