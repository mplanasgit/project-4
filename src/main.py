from flask import Flask, request, jsonify
import random
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as sql
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# -------------------------------------------------------------------------------------------------------------

app = Flask(__name__)

# Render the markdwon
@app.route("/")
def readme ():
    readme_file = open("../README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])

@app.route("/sentences/<name>")
def lines_from_character (name):
    return jsonify(sql.get_everything_from_character(name))

@app.route("/sa/<name>")
def sa_from_character (name):
    everything = sql.get_sentences(name)
    return jsonify([sia.polarity_scores(i["Sentence"])["compound"] for i in everything])

@app.route("/random/<name>")
def random_from_character (name):
    return jsonify(sql.get_random(name))





if __name__ == '__main__':
    app.run()