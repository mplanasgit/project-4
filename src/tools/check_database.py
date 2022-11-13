import pandas as pd

# GoT dataset
df = pd.read_csv("../data/got_script.csv")

# Dictionary to store seasons and episodes
season_episode = {season : set(episode) for season, episode in df.groupby('Season')['Episode']}
# List to store all unique characters
characters = [name for name in df['Name'].unique()]
# Number of characters
number_characters = len(characters)

# -------------------------------------------------------------------------------------------------------------
def check_season(season):
    '''This function checks if the inputed season is valid.
    '''
    if season.title() in season_episode.keys():
        return True
    else:
        return False

# -------------------------------------------------------------------------------------------------------------
def check_episode(season, episode):
    '''This function checks if the inputed episode is valid.
    '''
    if season.title() in season_episode and episode.title() in season_episode[season.title()]:
        return True
    else:
        return False

# -------------------------------------------------------------------------------------------------------------
def check_character(name):
    '''This function checks if the inputed character is valid.
    '''
    if name.title() in characters:
        return True
    else:
        return False

# -------------------------------------------------------------------------------------------------------------
def check_number_characters(number):
    '''This function checks if the number inputed is valid.
    '''
    if number <= number_characters:
        return True
    else:
        return False