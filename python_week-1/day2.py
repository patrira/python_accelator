number_hours_day = 24
units_hours = "hours"


def hours_in_days(num_of_days):
    if num_of_days > 0:
        return f"There are {num_of_days * number_hours_day} {units_hours} in {num_of_days} days"
    else:
        return "You have entered a negative number , so we cant convert for you"
    
    
n_days = input( "Enter number of days, then i will convert them into hours\n")

user_input_value= int(n_days)
calculated_result = hours_in_days(user_input_value)

print(calculated_result)

