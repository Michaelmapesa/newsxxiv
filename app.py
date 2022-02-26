from flask import Flask, render_template
from newsapi import NewsApiClient
app = Flask(__name__)
@app.route('/')
def index():
    #client apikey and id for authorization
    newsapi = NewsApiClient(api_key="e42fd1790bc54e73bb51cfcd7f903e9a")
    top_headlines = newsapi.get_top_headlines(sources="ktn-news")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)