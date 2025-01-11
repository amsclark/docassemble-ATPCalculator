def ei_consolidate(jobs):
  earned_income_total = 0
  for job in jobs:
     earned_income_total = earned_income_total + job.wage
  return earned_income_total

def get_employer_list(jobs):
  if len(jobs) == 1:
    return jobs[0].name.text
  if len(jobs) == 2:
    return jobs[0].name.text + " and " + jobs[1].name.text
  if len(jobs) > 2:
    english_list = ""
    for i in range(len(jobs) - 1):
      english_list = english_list + jobs[i].name.text + ", " 
    english_list = english_list + "and " + jobs[len(jobs) - 1].name.text
    return english_list
  else:
    return ""
    
def get_monthly_debts_text(monthly_housing, monthly_basic_utils, monthly_telecom_utils, monthly_real_estate_taxes_insurance, monthly_maint_repairs, monthly_housing_utils_total, monthly_delinquent_taxes, monthly_student_loans, monthly_child_support, monthly_alimony, monthly_court_debt_payments):
  debts_text_list = []
  debts_texts_joined = ""
  
  if monthly_housing > 0:
    debts_text_list.append("$" + str(monthly_housing) + " of monthly housing")
  if monthly_basic_utils > 0:
    debts_text_list.append("$" + str(monthly_basic_utils) + " of monthly basic utilities")
  if monthly_telecom_utils > 0:
    debts_text_list.append("$" + str(monthly_telecom_utils) + " of monthly telecom utilities")
  if monthly_real_estate_taxes_insurance > 0:
    debts_text_list.append("$" + str(monthly_real_estate_taxes_insurance) + " of monthly real estate taxes or insurance")
  if monthly_maint_repairs > 0:
    debts_text_list.append("$" + str(monthly_maint_repairs) + " of monthly home maintenance or repairs")
  if monthly_housing_utils_total > 0 and monthly_housing == 0 and monthly_basic_utils == 0 and monthly_telecom_utils == 0 and monthly_real_estate_taxes_insurance == 0:
    debts_text_list.append("$" + str(monthly_housing_utils_total) + " of total monthly housing utilities")
  if monthly_delinquent_taxes > 0:
    debts_text_list.append("$" + str(monthly_delinquent_taxes) + " of monthly delinquent taxes")
  if monthly_student_loans > 0:
    debts_text_list.append("$" + str(monthly_student_loans) + " of monthly student loans")
  if monthly_child_support > 0:
    debts_text_list.append("$" + str(monthly_child_support) + " of monthly child support")
  if monthly_alimony > 0:
    debts_text_list.append("$" + str(monthly_alimony) + " of monthly alimony")
  if monthly_court_debt_payments > 0:
    debts_text_list.append("$" + str(monthly_court_debt_payments) + " of monthly court debt payments")
  
  if len(debts_text_list) == 1:
    debts_texts_joined = debts_text_list[0]
    
  if len(debts_text_list) > 1:
    debts_text_list[-1] = " and " + debts_text_list[-1]
    debts_texts_joined = ", ".join(debts_text_list)
  
  return debts_texts_joined
  
def  get_monthly_expenses_text(monthly_food, monthly_housekeeping, monthly_apparel_and_service, monthly_personal_care, monthly_misc, monthly_operating, monthly_ownership, monthly_public_transit, monthly_housing, monthly_basic_utils, monthly_telecom_utils, monthly_real_estate_taxes_insurance, monthly_maint_repairs, monthly_housing_utils_total, monthly_health_insurance, monthly_oop_healthcare, monthly_medical_expenses, monthly_child_dependent_care, monthly_fica, monthly_est_tax_payments, monthly_term_life_insurance, monthly_retirement_required, monthly_retirement_voluntary, monthly_union_dues, monthly_other):
  expense_text_list = []
  expense_text_joined = ""
  
  if monthly_food > 0:
    expense_text_list.append("$" + str(monthly_food) + " of monthly food expenses")
  if monthly_housekeeping > 0:
    expense_text_list.append("$" + str(monthly_housekeeping) + " of monthly housekeeping expenses")
  if monthly_apparel_and_service > 0:
    expense_text_list.append("$" + str(monthly_apparel_and_service) + " of monthly apparel and services expenses")
  if monthly_personal_care > 0:
    expense_text_list.append("$" + str(monthly_personal_care) + " of monthly personal care expenses")
  if monthly_misc > 0:
    expense_text_list.append("$" + str(monthly_misc) + " of monthly miscellaneous expenses")
  if monthly_operating > 0:
    expense_text_list.append("$" + str(monthly_operating) + " of monthly vehicle operating expenses")
  if monthly_ownership > 0:
    expense_text_list.append("$" + str(monthly_ownership) + " of monthly vehicle ownership expenses")
  if monthly_public_transit > 0:
    expense_text_list.append("$" + str(monthly_public_transit) + " of monthly public transportation expenses")
  if monthly_housing > 0:
    expense_text_list.append("$" + str(monthly_housing) + " of monthly rent/mortgage/housing expenses")
  if monthly_basic_utils > 0:
    expense_text_list.append("$" + str(monthly_basic_utils) + " of monthly electric, oil/gas, Water/Trash expenses")
  if monthly_telecom_utils > 0:
    expense_text_list.append("$" + str(monthly_telecom_utils) + " of monthly phone/cell/cable/internet expenses")
  if monthly_real_estate_taxes_insurance > 0:
    expense_text_list.append("$" + str(monthly_real_estate_taxes_insurance) + " of real estate taxes & insurance expenses")
  if monthly_maint_repairs > 0:
    expense_text_list.append("$" + str(monthly_maint_repairs) + " of monthly monthly maintenance & repairs expenses")
  if monthly_housing_utils_total > 0:
    expense_text_list.append("$" + str(monthly_housing_utils_total) + " of total monthly housing expenses")
  if monthly_health_insurance > 0:
    expense_text_list.append("$" + str(monthly_health_insurance) + " of monthly health insurance expenses")
  if monthly_oop_healthcare > 0:
    expense_text_list.append("$" + str(monthly_oop_healthcare) + " of monthly out of pocket healthcare expenses")
  if monthly_medical_expenses > 0:
    expense_text_list.append("$" + str(monthly_medical_expenses) + " of monthly medical expenses")
  if monthly_child_dependent_care > 0:
    expense_text_list.append("$" + str(monthly_child_dependent_care) + " of monthly child/dependent care expenses")
  if monthly_fica > 0:
    expense_text_list.append("$" + str(monthly_fica) + " of monthly FICA payments")
  if monthly_est_tax_payments > 0:
    expense_text_list.append("$" + str(monthly_est_tax_payments) + " of monthly estimated tax payments")
  if monthly_term_life_insurance > 0:
    expense_text_list.append("$" + str(monthly_term_life_insurance) + " of monthly term life insurance expenses")
  if monthly_retirement_required > 0:
    expense_text_list.append("$" + str(monthly_retirement_required) + " of monthly employer-required retirement expenses")
  if monthly_retirement_voluntary > 0:
    expense_text_list.append("$" + str(monthly_retirement_voluntary) + " of monthly voluntary retirement expenses")
  if monthly_union_dues > 0:
    expense_text_list.append("$" + str(monthly_union_dues) + " of monthly union dues")
  if monthly_other > 0:
    expense_text_list.append("$" + str(monthly_other) + " of other monthly expenses")
  
  if len(expense_text_list) == 1:
    expense_text_joined = expense_text_list[0]
    
  if len(expense_text_list) > 1:
    expense_text_list[-1] = " and " + expense_text_list[-1]
    expense_text_joined = ", ".join(expense_text_list)
  
  return expense_text_joined



 



def get_other_income_list(not_jobs, state, oi_labels, tanf_alt_names):
  oi_labels["inc_tanf"] = tanf_alt_names.get(state, "TANF")
  if len(not_jobs) == 1:
    return "$" + str(not_jobs[0].amount) + " monthly from " + oi_labels[not_jobs[0].name.text]
  if len(not_jobs) == 2:
    return "$" + str(not_jobs[0].amount) + " monthly from " + oi_labels[not_jobs[0].name.text] + " and $" + str(not_jobs[1].amount) + " monthly from " + oi_labels[not_jobs[1].name.text]
  if len(not_jobs) > 2:
    english_list = ""
    for i in range(len(not_jobs) - 1):
      english_list = english_list + "$" + str(not_jobs[i].amount) + " monthly from " + oi_labels[not_jobs[i].name.text] + ", "
    english_list = english_list + "and $" + str(not_jobs[len(not_jobs) - 1].amount) + " monthly from " + oi_labels[not_jobs[len(not_jobs) - 1].name.text]
    return english_list
  else:
    return ""
    
def oi_consolidate(not_jobs):
  oi_totals = {"inc_SS": 0, 
               "inc_unemp": 0, 
               "inc_VA": 0, 
               "inc_tanf": 0, 
               "inc_pens": 0, 
               "inc_snap": 0, 
               "inc_alim": 0, 
               "inc_invest": 0, 
               "inc_other_other": 0,
               "inc_oi_total": 0
              }
  for not_job in not_jobs:
    oi_totals['inc_oi_total'] = oi_totals['inc_oi_total'] + not_job.amount
    if not_job.name.text == 'inc_ss':
      oi_totals['inc_ss'] = oi_totals['inc_ss'] + not_job.amount
      
    if not_job.name.text == 'inc_unemp':
      oi_totals['inc_unemp'] = oi_totals['inc_unemp'] + not_job.amount
      
    if not_job.name.text == 'inc_VA':
      oi_totals['inc_VA'] = oi_totals['inc_VA'] + not_job.amount
      
    if not_job.name.text == 'inc_tanf':
      oi_totals['inc_tanf'] = oi_totals['inc_tanf'] + not_job.amount
      
    if not_job.name.text == 'inc_pens':
      oi_totals['inc_pens'] = oi_totals['inc_pens'] + not_job.amount
      
    if not_job.name.text == 'inc_snap':
      oi_totals['inc_snap'] = oi_totals['inc_snap'] + not_job.amount
      
    if not_job.name.text == 'inc_alim':
      oi_totals['inc_alim'] = oi_totals['inc_alim'] + not_job.amount
      
    if not_job.name.text == 'inc_invest':
      oi_totals['inc_invest'] = oi_totals['inc_invest'] + not_job.amount

    if not_job.name.text == 'inc_other_other':
      oi_totals['inc_other_other'] = oi_totals['inc_other_other'] + not_job.amount
  return oi_totals