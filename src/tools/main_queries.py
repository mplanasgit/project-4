# Libraries
import requests
from pandas import json_normalize
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# -------------------------------------------------------------------------------------------------------------
# Function to get a df of the top characters by number of sentences
def get_my_top_characters(url = "http://127.0.0.1:5000/top"):
    '''This function requests a local API for the top characters of GoT based on their number of lines in the show.
    Args
    :url: str. your local port.
    Returns
    :df: dataframe. Contains the number of sentences by character
    '''
    endpoint = url
    response = requests.get(endpoint)
    df = json_normalize(response.json())
    return df

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
# Function to get a df of the sentiment analysis of a character for the entire show
def sa_by_character_mean(names, url = "http://127.0.0.1:5000/script/sa/character/mean/"):
    # To store the sentiments
    dict_of_sa = {}
    for n in names:
        endpoint = url + f"{n}"
        try:
            response = requests.get(endpoint).json()
        except:
            return "Oops! There was an error in your request. Check our docs for the supported character names."
        dict_of_sa[n.title()] = response
    
    df = pd.DataFrame(list(dict_of_sa.items())).rename(columns = {0:'Name', 1:'Mean Compound'}).sort_values(by=["Mean Compound"]) 

    return df

# -------------------------------------------------------------------------------------------------------------
# Function to get a df of the sentiment analysis of a character for the specified seasons
def sa_by_seasons(seasons, name, url = "http://127.0.0.1:5000/script/sa/"):
    '''This function requests a local API for the script of your GoT character.
    Args
    :season: list of str. specify the seasons in the format: "season 1", "season 2",...
    :name: str. specify the character name in the format: "jon snow", "arya stark",..
    :url: str. your local port.
    Returns
    :df: dataframe. Contains the sentiment analysis of the character for the specified seasons.
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


# -------------------------------------------------------------------------------------------------------------
# Function to get a df of the sentiment analysis of a character for the specified seasons
def sa_by_seasons_mean(seasons, names, stop = "", url = "http://127.0.0.1:5000/script/sa/"):
    '''This function requests a local API for the script of your GoT character.
    Args
    :seasons: list of str. specify the seasons in the format: "season 1", "season 2",...
    :names: list of str. specify the character names in the format: "jon snow", "arya stark",..
    :url: str. your local port.
    Returns
    :df: dataframe. Contains the sentiment analysis mean for the specified seasons.
    '''
    # To store the sentiments of each character
    dict_of_sa = {}

    for n in names:
        sa_of_character = {}
        # Seasons is a list with all the seasons to include in the request
        for s in seasons:
            endpoint = url + f"{s}/mean{stop}/character/{n}"
            try:
                response = requests.get(endpoint).json()
            except:
                return "Oops! There was an error in your request. Check our docs for the supported season, episode, and character names."
            sa_of_character[s.title()] = response
        dict_of_sa[n.title()] = sa_of_character
    
    df = pd.DataFrame(dict_of_sa)

    return df

# -------------------------------------------------------------------------------------------------------------
# Function to get a df of the sentiment analysis of a character for the specified episodes
def sa_by_episodes_mean(season, episode, names, stop = "", url = "http://127.0.0.1:5000/script/sa/"):
    '''This function requests a local API for the script of your GoT character.
    Args
    :season: str. specify the season in the format: "season 1", "season 2",...
    :names: list of str. specify the character names in the format: "jon snow", "arya stark",...
    :episodes: list of str. specify the episodes in the format: "episode 1", "episode 2",...
    :url: str. your local port.
    Returns
    :df: dataframe. Contains the sentiment analysis mean for the specified episodes.
    '''
    # To store the sentiments of each character
    dict_of_sa = {}

    for n in names:
        sa_of_character = {}
        # Seasons is a list with all the seasons to include in the request
        for e in episode:
            endpoint = url + f"{season}/{e}/mean{stop}/character/{n}"
            try:
                response = requests.get(endpoint).json()
            except:
                return "Oops! There was an error in your request. Check our docs for the supported season, episode, and character names."
            sa_of_character[e.title()] = response
        dict_of_sa[n.title()] = sa_of_character
    
    df = pd.DataFrame(dict_of_sa)

    return df

# -------------------------------------------------------------------------------------------------------------
# Function to get a df of all the sentences of a character for the entire show
def sentences_by_character(names, url = "http://127.0.0.1:5000/script/character/sentences/"):
    # To store the sentences
    dict_of_sentences = {}
    for n in names:
        endpoint = url + f"{n}"
        try:
            response = requests.get(endpoint).json()
        except:
            return "Oops! There was an error in your request. Check our docs for the supported character names."
        dict_of_sentences[n.title()] = response
    
    df = pd.DataFrame(list(dict_of_sentences.items())).rename(columns = {0:'Name', 1:'Sentence'})

    return df

# -------------------------------------------------------------------------------------------------------------
# Function to clean sentences from sentences_by_character df
def clean_sentences(df, name):
    list_sentences = []
    for sentence in df.loc[df['Name'] == name]['Sentence'].values[0]:
        list_sentences.append(sentence['Sentence'])
    script = " ".join(list_sentences)
    return script
