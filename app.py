from importlib.resources import contents
from py_compile import main
from flask import Flask, render_template
from newsapi import NewsApiClient
app = Flask(__name__)
@app.route('/')
def index():
    #client apikey and id for authorization
    newsapi = NewsApiClient(api_key="e42fd1790bc54e73bb51cfcd7f903e9a")
    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
   
    #fetching articles for top headlines
    #make a list of content to store values on the list

    t_articles = top_headlines['articles']
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #function to fetch all the content
    for i in range(len(t_articles)):
        main_articles= t_articles[i]

        #appending list
        news.append(main_articles['title'])
        desc.append(main_articles['description'])
        img.append(main_articles['urlToImage'])
        p_date.append(main_articles['publishedAt'])
        url.append(main_articles['url'])
        contents = zip(news,desc,img,p_date,url)

        return render_template('index.html',contents=contents)


if __name__ == '__main__':
    app.run(debug=True)