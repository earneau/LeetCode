# Link to the exercise : https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

############ INSTRUCTIONS ##############
########################################

# Table Activities:

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | sell_date   | date    |
# | product     | varchar |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.

# Write a solution to find for each date the number of different products sold and their names.
# The sold products names for each date should be sorted lexicographically.

# Return the result table ordered by sell_date.


############### EXERCISE ###############
########################################

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date').agg({'product': ['nunique', lambda x: ','.join(sorted(set(x)))]}).reset_index()
    df.columns = ['sell_date', 'num_sold', 'products']
    return df