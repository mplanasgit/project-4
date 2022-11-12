# Libraries
import requests
from pandas import json_normalize

# -------------------------------------------------------------------------------------------------------------
# Function to get the script of a character
def get_my_character(season, episode, character, url = "http://127.0.0.1:5000/script/"):
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
    endpoint = url + f"{season}/{episode}/{character}"
    
    # Get the response as df
    response = requests.get(endpoint)
    
    try:
        df = json_normalize(response.json())
    except:
        return "Oops! There was an error in your request. Check our docs for the supported season, episode, and character names."
    
    return df