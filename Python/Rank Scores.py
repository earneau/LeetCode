# Link to the exercise : https://leetcode.com/problems/rank-scores/description/?lang=pythondata

############ INSTRUCTIONS ##############
########################################

# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

# The result format is in the following example.

############### EXERCISE ###############
########################################

# sliding window approach 

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)   # using dense method allows us to have no gaps in id ranking after a tie
    df_sorted = scores.sort_values(by='score', ascending=False)     # sorting from best to worst score
    return df_sorted[['score', 'rank']]     # reshaping, using only score and rank columns as id is now useless