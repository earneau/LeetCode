# Link to the exercise : https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

############ INSTRUCTIONS ##############
########################################

# Table: Views

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.

# Write a solution to find all the authors that viewed at least one of their own articles.

# Return the result table sorted by id in ascending order.

############### EXERCISE ###############
########################################

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']]
    result = pd.DataFrame(views['author_id'].unique(), columns=['id'])
    return result.sort_values(by='id', ascending=True)