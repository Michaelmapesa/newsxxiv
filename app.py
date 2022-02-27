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
    #all main articles
    all_articles = newsapi.get_everything(sources="bbc-news")
   
    #fetching articles for top headlines
    #make a list of content to store values on the list
    t_articles = top_headlines['articles']
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    #fetching all articles of all article news
    a_articles = all_articles['articles']
    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    #function to fetch all the content
    for i in range(len(t_articles)):
        main_article= t_articles[i]

    #function to fetch all the content in everything
    for j in range(len(a_articles)):
        a_articles=a_articles[j]

        #appending list
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        contents = zip(news,desc,img,p_date,url)

        #appending list all
        news_all.append(a_articles['title'])
        desc_all.append(a_articles['description'])
        img_all.append(a_articles['urlToImage'])
        p_date_all.append(a_articles['publishedAt'])
        url_all.append(a_articles['url'])
        all = zip(news_all,desc_all,img_all,p_date_all,url_all)

        #pass in the rendered files
        return render_template('index.html',contents=contents,all=all)


if __name__ == '__main__':
    app.run(debug=True)