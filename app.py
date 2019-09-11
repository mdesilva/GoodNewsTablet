from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, render_template
import requests

app = Flask(__name__)

def parseArticles():
    data = requests.get("https://www.goodnewsnetwork.org/")
    soup = BeautifulSoup(data.text, features="lxml")
    articles = []
    rawArticles = soup.find_all(attrs={"class": "td-module-thumb"})
    for article in range(0,9):
        articleHtml = rawArticles[article].find("a")
        title = articleHtml['title']
        link = articleHtml['href']
        imgSrc = articleHtml.contents[0]['src'].replace("-218x150", "") #assuming that all thumnails are 218x150px 
        articleContent = {"title": title, "link": link, "img": imgSrc}
        articles.append(articleContent)
    return articles

@app.route("/api/articles", methods=["GET"])
def getArticlesJSON():
    return jsonify(parseArticles())

@app.route("/articles", methods=["GET"])
def getArticles():
    articles = parseArticles()
    return render_template('index.html', articles=articles)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)