# Libraries
import requests
from pandas import json_normalize
import pandas as pd
import numpy as np

# -------------------------------------------------------------------------------------------------------------
# Function to get a df of the script of a character for a given episode
def get_my_character(season, episode, name, url = "http://127.0.0.1:5000/script/"):
    '''This function requests a local API for the script of your GoT character.
    Args
    :season: str. specify the season in the format: "season 1", "season 2",...
    :episode: str. specify the episode in the format: "episode 1", "episode 2",...
    :character: str. specify the character in the format: "jon snow", "arya stark",..
    :url: str. your local port.
    Returns
    :df: dataframe. Contains the sentences of the character for the specified episode.
    '''
    # Specify endpoint
    endpoint = url + f"{season}/{episode}/{name}"
    
    # Get the response as df
    response = requests.get(endpoint)
    
    try:
        df = json_normalize(response.json())
    except:
        return "Oops! There was an error in your request. Check our docs for the supported season, episode, and character names."
    
    return df

# -------------------------------------------------------------------------------------------------------------
# Function to get a df of the sentiment analysis of a character for a given season
def get_my_character_by_season(season, name, url = "http://127.0.0.1:5000/script/sa/"):
    '''This function requests a local API for the script of your GoT character.
    Args
    :season: str. specify the season in the format: "season 1", "season 2",...
    :episode: str. specify the episode in the format: "episode 1", "episode 2",...
    :name: str. specify the character name in the format: "jon snow", "arya stark",..
    :url: str. your local port.
    Returns
    :
    '''
    # Specify endpoint
    endpoint = url + f"{season}/character/{name}"
    
    try:
        response = requests.get(endpoint)
        return response.json()
    except:
        return "Oops! There was an error in your request. Check our docs for the supported season, episode, and character names."





# Function to get a df of the sentiment analysis of a character for a given season
def get_my_character_by_seasons(seasons, name, url = "http://127.0.0.1:5000/script/sa/"):
    '''This function requests a local API for the script of your GoT character.
    Args
    :season: list of str. specify the seasons in the format: "season 1", "season 2",...
    :name: str. specify the character name in the format: "jon snow", "arya stark",..
    :url: str. your local port.
    Returns
    :df: dataframe. Contains the sentences of the character for the specified episode.
    '''
    # To store the sentiments
    dict_of_sa = {}

    # Seasons is a list with all the seasons to include in the request
    for s in seasons:
        endpoint = url + f"{s}/character/{name}"
        try:
            response = requests.get(endpoint).json()
        except:
            return "Oops! There was an error in your request. Check our docs for the supported season, episode, and character names."
        dict_of_sa[s.title()] = response
    
    df = json_normalize(dict_of_sa).T.reset_index().rename(columns = {'index': 'Season', 0: "compound"})
    df['compound_mean'] = df['compound'].apply(lambda x: np.mean(x))

    return df

