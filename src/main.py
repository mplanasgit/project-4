from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as sql
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# ------------------------------------------------------------------------------------------------------- FLASK

app = Flask(__name__)

# ------------------------------------------------------------------------------------------------------ README
# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("../README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

# ------------------------------------------------------------------------------------------------- GET SCRIPTS
# Returns a random sequence from a character
@app.route("/random/<name>")
def random_from_character (name):
    return jsonify(sql.get_random(name))

# -------------------------------------------------------------------------------------------------------------
# Get the entire script of the show (returns the entire table in the database)
@app.route("/script")
def get_show_script():
    return jsonify(sql.get_script())

# -------------------------------------------------------------------------------------------------------------
# Get the script of the entire show for a specified character
@app.route("/script/character/<name>")
def script_from_character (name):
    return jsonify(sql.get_script_from_character(name))

# -------------------------------------------------------------------------------------------------------------
# Get the script of an entire season
@app.route("/script/<season>")
def season_script (season):
    return jsonify(sql.get_script_from_season(season))

# -------------------------------------------------------------------------------------------------------------
# Get the script of an episode of a given season
@app.route("/script/<season>/<episode>")
def episode_script (season, episode):
    return jsonify(sql.get_script_from_episode(season, episode))

# -------------------------------------------------------------------------------------------------------------
# Get the script of a character for a given episode of a season
@app.route("/script/<season>/<episode>/<name>")
def character_script_by_episode (season, episode, name):
    return jsonify(sql.get_character_script_from_episode(season, episode, name))

# ----------------------------------------------------------------------------------------------- GET SENTIMENT
# Get the sentiment analysis (sa) of all the sentences of a character (entire show)
@app.route("/script/sa/character/<name>")
def sa_from_character (name):
    sentences = sql.get_script_from_character(name)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

# -------------------------------------------------------------------------------------------------------------
# Get the SA of all the sentences of a season
@app.route("/script/sa/<season>")
def sa_from_season (season):
    sentences = sql.get_script_from_season(season)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in sentences])

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



if __name__ == '__main__':
    app.run()