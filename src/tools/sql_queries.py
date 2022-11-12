from config.sql_connection import engine
import pandas as pd

# -------------------------------------------------------------------------------------------------------------
# Function that returns a random sentence from the specified character

def get_random (name):
    query = f"""SELECT Season, Episode, Name, Sentence 
    FROM got_script
    WHERE Name = '{name}'
    ORDER BY RAND()
    LIMIT 1;"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function to get everything from the show (returns the entire table)

def get_script():
    query = """SELECT *
    FROM got_script;"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function to get everything of a character

def get_script_from_character (name):
    query = f"""SELECT ID, Season, Episode, `Episode Title`, Name, Sentence 
    FROM got_script
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    
    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function to get the script of a season

def get_script_from_season (season):
    query = f"""SELECT ID, Season, Episode, `Episode Title`, Name, Sentence 
    FROM got_script
    WHERE Season = '{season}';"""

    df = pd.read_sql_query(query, engine)
    
    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function to get the script of an episode

def get_script_from_episode (season, episode):
    query = f"""SELECT ID, Season, Episode, `Episode Title`, Name, Sentence 
    FROM got_script
    WHERE Season = '{season}'
    AND Episode = '{episode}';"""

    df = pd.read_sql_query(query, engine)
    
    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function to get the script of a character for a given episode

def get_character_script_from_episode (season, episode, name):
    query = f"""SELECT ID, Season, Episode, `Episode Title`, Name, Sentence
    FROM got_script
    WHERE Season = '{season}'
    AND Episode = '{episode}'
    AND Name = '{name}';"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function to get all the sentences of a character

def get_sentences (name):
    query = f"""SELECT Sentence 
    FROM got_script
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")


# -------------------------------------------------------------------------------------------------------------
