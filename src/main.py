from flask import Flask, request, jsonify
import markdown.extensions.fenced_code
import tools.sql_queries as sql
import tools.check_database as che
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
sia = SentimentIntensityAnalyzer()

# ------------------------------------------------------------------------------------------------------- FLASK

app = Flask(__name__)

# ------------------------------------------------------------------------------------------------------ README
# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("../README_API.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# ----------------------------------------------------------------------------------------------------- GET TOP
# Get the top characters by total number of sentences in the show
@app.route("/top")
def get_top_characters ():
    return jsonify(sql.get_top())

# ------------------------------------------------------------------------------------------------- GET SCRIPTS
# Returns a random sequence from a character
@app.route("/random/<name>")
def random_from_character (name):
    if che.check_character(name):
        sentence = jsonify(sql.get_random(name))
        return sentence
    else:
        return "The specified character is not valid. Refer to our docs for the names of the characters."

# -------------------------------------------------------------------------------------------------------------
# Get the entire script of the show (returns the entire table in the database)
@app.route("/script")
def get_show_script():
    return jsonify(sql.get_script())

# -------------------------------------------------------------------------------------------------------------
# Get the script of the entire show for a specified character
@app.route("/script/character/<name>")
def script_from_character (name):
    if che.check_character(name):
        return jsonify(sql.get_script_from_character(name))
    else:
        return "The specified character is not valid. Refer to our docs for the names of the characters."

# -------------------------------------------------------------------------------------------------------------
# Get the sentences of the entire show for a specified character
@app.route("/script/character/sentences/<name>")
def sentences_from_character (name):
    if che.check_character(name):
        return jsonify(sql.get_sentences(name))
    else:
        return "The specified character is not valid. Refer to our docs for the names of the characters."

# -------------------------------------------------------------------------------------------------------------
# Get the script of an entire season
@app.route("/script/<season>")
def season_script (season):
    if che.check_season(season):
        return jsonify(sql.get_script_from_season(season))
    else:
        return "The specified season is not valid. Please specify the season in the following format: season N , where N is a number from 1 to 8."

# -------------------------------------------------------------------------------------------------------------
# Get the script of a character of an entire season
@app.route("/script/<season>/character/<name>")
def character_script_by_season (season, name):
    if che.check_season(season):
        if che.check_character(name):
            return jsonify(sql.get_character_script_from_season(season, name))
        else:
            return "The specified character is not valid. Refer to our docs for the names of the characters."
    else:
        return "The specified season is not valid. Please specify the season in the following format: season N , where N is a number from 1 to 8."

# -------------------------------------------------------------------------------------------------------------
# Get the script of an episode of a given season
@app.route("/script/<season>/<episode>")
def episode_script (season, episode):
    if che.check_season(season):
        if che.check_episode(season, episode):
            return jsonify(sql.get_script_from_episode(season, episode))
        else:
            return "The specified episode is not valid. Please specify the episode in the following format: episode N , where N is a number from 1 to 10 for Seasons 1 to 6. Season 7 consists of 7 episodes, and Season 8 consists of 6 episodes."
    else:
        return "The specified season is not valid. Please specify the season in the following format: season N , where N is a number from 1 to 8."

# -------------------------------------------------------------------------------------------------------------
# Get the script of a character for a given episode of a season
@app.route("/script/<season>/<episode>/<name>")
def character_script_by_episode (season, episode, name):
    if che.check_season(season):
        if che.check_episode(season, episode):
            if che.check_character(name):
                return jsonify(sql.get_character_script_from_episode(season, episode, name))
            else:
                return "The specified character is not valid. Refer to our docs for the names of the characters."
        else:
            return "The specified episode is not valid. Please specify the episode in the following format: episode N , where N is a number from 1 to 10 for Seasons 1 to 6. Season 7 consists of 7 episodes, and Season 8 consists of 6 episodes."
    else:
        return "The specified season is not valid. Please specify the season in the following format: season N , where N is a number from 1 to 8."

# -------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------- GET SENTIMENT
# Get the sentiment analysis (sa) of all the sentences of a character (entire show)
@app.route("/script/sa/character/<name>")
def sa_from_character (name):
    sentences = sql.get_script_from_character(name)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

# -------------------------------------------------------------------------------------------------------------
# Get the MEAN sentiment analysis (sa) of all the sentences of a character
@app.route("/script/sa/character/mean/<name>")
def sa_from_character_mean (name):
    sentences = sql.get_script_from_character(name)
    sa = [sia.polarity_scores(i["Sentence"])["compound"] for i in sentences]
    mean_sa = np.mean(sa)
    return jsonify(mean_sa)

# -------------------------------------------------------------------------------------------------------------
# Get the SA of all the sentences of a season
@app.route("/script/sa/<season>")
def sa_from_season (season):
    sentences = sql.get_script_from_season(season)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

# -------------------------------------------------------------------------------------------------------------
# Get the SA of all the sentences of a character of a season
@app.route("/script/sa/<season>/character/<name>")
def sa_from_character_by_season (season, name):
    sentences = sql.get_character_script_from_season(season, name)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

# -------------------------------------------------------------------------------------------------------------
# Get the MEAN SA of all the sentences of a character of a season by espisode
@app.route("/script/sa/<season>/<episode>/mean/character/<name>")
def sa_from_character_by_episode_mean (season, episode, name):
    # Get sentences
    sentences = sql.get_character_script_from_episode (season, episode, name)
    sa = [sia.polarity_scores(i["Sentence"])["compound"] for i in sentences]
    mean_sa = np.mean(sa)
    return jsonify(mean_sa)

# -------------------------------------------------------------------------------------------------------------
# Get the MEAN SA of all the sentences of a character of a season
@app.route("/script/sa/<season>/mean/character/<name>")
def sa_from_character_by_season_mean (season, name):
    # Get sentences
    sentences = sql.get_character_script_from_season(season, name)
    sa = [sia.polarity_scores(i["Sentence"])["compound"] for i in sentences]
    mean_sa = np.mean(sa)
    return jsonify(mean_sa)

# -------------------------------------------------------------------------------------------------------------
# Get the MEAN SA of all the sentences of a character of a season after removing stop words
@app.route("/script/sa/<season>/meanstop/character/<name>")
def sa_from_character_by_season_meanstop (season, name):
    # Get sentences
    sentences = sql.get_character_script_from_season(season, name)
    # Set of stop words, symbols to remove
    stop_words = set(stopwords.words('english'))
    symbols = ['?', '!', ',', '.', "'re", "'ve", "'s", "'m"]
    # Store sentiment in list
    sa_list = []
    for sen in sentences:
        # Tokenize words of each sentence
        sentence_tokenized = word_tokenize(sen["Sentence"])
        # Keep non stop words and filter out symbols
        sentence_without_stop = [w for w in sentence_tokenized if not w.lower() in stop_words]
        filtered_sentence = " ".join([w for w in sentence_without_stop if not w.lower() in symbols])
        # Apply sentiment
        sa = sia.polarity_scores(filtered_sentence)["compound"]
        sa_list.append(sa)

    # Calculate the mean sentiment of the season
    mean_sa = np.mean(sa_list)

    return jsonify(mean_sa)

# -------------------------------------------------------------------------------------------------------------
# Get the SA of all the sentences of an episode
@app.route("/script/sa/<season>/<episode>")
def sa_from_episode (season, episode):
    sentences = sql.get_script_from_episode(season, episode)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

# -------------------------------------------------------------------------------------------------------------
# Get the SA of the sentences of a character in a given episode
@app.route("/script/sa/<season>/<episode>/<name>")
def sa_from_character_by_episode (season, episode, name):
    sentences = sql.get_character_script_from_episode(season, episode, name)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

# -------------------------------------------------------------------------------------------------------- POST
# Request a post
@app.route("/insertrow", methods=["POST"])
def insert_row ():
    #??Decoding params
    my_params = request.args
    id = my_params["ID"]
    release_date = my_params["Release Date"]
    season = my_params["Season"]
    episode = my_params["Episode"]
    episode_title = my_params["Episode Title"]
    name = my_params["Name"]
    sentence = my_params["Sentence"]

    # Passing to my function: do the insert
    sql.insert_one_row(id, release_date, season, episode, episode_title, name, sentence)
    return f"Query succesfully inserted"

# -------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()