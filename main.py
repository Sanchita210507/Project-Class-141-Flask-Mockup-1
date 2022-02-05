from flask import Flask, jsonify

import csv
all_articles = []
with open("articles.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_read = []

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Homepage!"

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"

    })

@app.route("/liked_article", methods = ["POST"])
def liked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }), 200

@app.route("/unliked_article", methods = ["POST"])
def unliked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }), 200

@app.route("/did_not_read", methods = ["POST"])
def did_not_read():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_read().append(article)
    return jsonify({
        "status":"success"
    }), 200


if __name__ == "__main__":
    app.run(debug = True)
