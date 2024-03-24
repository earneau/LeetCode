# Link to the exercise : https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

############ INSTRUCTIONS ##############
########################################

# Table: Employees

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.

# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

# Return the result table ordered by employee_id.

############### EXERCISE ###############
########################################

import pandas as pd

def bonus(employee_id, name, salary):
    if (not name.startswith('M')) and (employee_id % 2 != 0):
        return salary
    else:
        return 0

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.apply(lambda row: bonus(row['employee_id'], row['name'], row['salary']), axis=1)
    bonus_df = pd.DataFrame({'employee_id': employees['employee_id'], 'bonus': result})
    return bonus_df.sort_values(by = 'employee_id', ascending = True)