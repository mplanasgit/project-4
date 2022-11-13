from config.sql_connection import engine
import pandas as pd

# -------------------------------------------------------------------------------------------------------------
# Function to get the top N characters by number of sentences in the show
# Didn't work when asking to input the LIMIT number.
def get_top ():
    query = f"""SELECT Name, count('Sentence') as 'Number of sentences' 
    FROM got_script
    GROUP BY Name
    ORDER BY count('Sentence') DESC;"""
    
    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")

# -------------------------------------------------------------------------------------------------------------
# Function that returns a random sentence from the specified character

def get_random (name):
    query = f"""SELECT Sentence 
    FROM got_script
    WHERE Name = '{name}'
    ORDER BY RAND()
    LIMIT 1;"""

    df = pd.read_sql_query(query, engine)
    sentence = df.to_dict(orient="records")

    return sentence[0]['Sentence']

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
# Function to get the script of a character of an entire season

def get_character_script_from_season (season, name):
    query = f"""SELECT ID, Season, Episode, `Episode Title`, Name, Sentence 
    FROM got_script
    WHERE Season = '{season}'
    AND Name = '{name}';"""

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
# Function to insert a row into a table

def insert_one_row (id, release_date, season, episode, episode_title, name, sentence):
    query = f"""INSERT INTO got_script
     (ID, `Release Date`, Season, Episode, `Episode Title`, Name, Sentence) 
        VALUES ({id}, '{release_date}', '{season}', '{episode}', '{episode_title}', '{name}', '{sentence}');
    """
    engine.execute(query)
    return f"Correctly introduced!"