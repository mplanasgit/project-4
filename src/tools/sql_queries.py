from config.sql_connection import engine
import pandas as pd

# -------------------------------------------------

def get_everything_from_character (name):
    query = f"""SELECT * 
    FROM got_script
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)
    
    return df.to_dict(orient="records")


def get_sentence (name):
    query = f"""SELECT Sentence 
    FROM got_script
    WHERE Name = '{name}';"""

    df = pd.read_sql_query(query, engine)

    return df.to_dict(orient="records")