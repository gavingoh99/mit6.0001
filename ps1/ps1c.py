starting_salary = float(input('Enter the starting salary: '))
cost_of_house = 1000000
semi_annual_raise = 0.07
annual_return_of_investment = 0.04
down_payment = 0.25 * cost_of_house
epsilon = 100
low = 0
high = 10000
steps = 0

while True:
    portion_saved = (high + low) / 2
    current_savings = 0
    for month in range(0, 36):
        monthly_salary = starting_salary / 12
        current_savings = current_savings + (current_savings * 0.04)/12 + float((portion_saved * monthly_salary)/10000)
        if month % 6 == 0:
            monthly_salary = (1 + semi_annual_raise) * monthly_salary
    if abs(current_savings - down_payment) <= epsilon:
        print('Best savings rate: ', '%.2f' % (portion_saved / 100), '%')
        print('Steps in bisection search: ', steps)
        break
    elif abs(current_savings - down_payment) > epsilon and current_savings > down_payment:
        high = portion_saved
    elif abs(current_savings - down_payment) > epsilon and current_savings < down_payment:
        low = portion_saved
    if low == high:
        print('It is not possible to pay the down payment in three years')
        break
    steps += 1


    