annual_salary_input = input('Enter your annual salary: ')
portion_saved_input = input('Enter the percent of your salary to save, as a decimal: ')
total_cost_input = input('Enter the cost of your dream home: ')
semi_annual_raise_input = input('Enter the semi-annual raise, as a decimal: ')

annual_salary = float(annual_salary_input)
portion_saved = float(portion_saved_input)
total_cost = float(total_cost_input)
semi_annual_raise = float(semi_annual_raise_input)

portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary / 12
months = 0

while current_savings < portion_down_payment:
    current_savings = current_savings * 12.04 / 12 + portion_saved * monthly_salary
    months += 1
    if months % 6 == 0:
        monthly_salary = (1 + semi_annual_raise) * monthly_salary
print('Number of months:', months)