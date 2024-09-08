# Link to the exercise : https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

############ INSTRUCTIONS ##############
########################################

# Write a solution to find the first login date for each player.
# Return the result table in any order.
# The result format is in the following example.

############### EXERCISE ###############
########################################

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    first_login.columns = ['player_id', 'first_login']
    return first_login