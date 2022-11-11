from config.sql_connection import engine
import pandas as pd

# ----------------------------------------------------------------------
# Function to get the whole script from a character

def get_everything_from_character (name):
    query = f"""SELECT * 
    FROM got_script
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    
    return df.to_dict(orient="records")

# ----------------------------------------------------------------------
# Function to get the script from a season

def get_script_from_season (season):
    query = f"""SELECT * 
    FROM got_script
    WHERE Season = '{season}';"""

    df = pd.read_sql_query(query, engine)
    
    return df.to_dict(orient="records")

# ----------------------------------------------------------------------
# Function to get the entire script of a character

def get_sentences (name):
    query = f"""SELECT Sentence 
    FROM got_script
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")

# -----------------------------------------------------------------------
# Function that returns a random sentence from the specified character

def get_random (name):
    query = f"""SELECT Sentence 
    FROM got_script
    WHERE Name = '{name}'
    ORDER BY RAND()
    LIMIT 1;"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")    