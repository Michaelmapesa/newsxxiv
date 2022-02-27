from importlib.resources import contents
from py_compile import main
from flask import Flask, render_template
from newsapi import NewsApiClient
from .config import Config
import urllib.request,json

api_key=None
base_url=None
base_url_for_everything=None
base_url_top_headlines=None
def topHeadlines():
    #client apikey and id for authorization
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    top_headlines = newsapi.get_top_headlines(sources="bbc-news")
    
    #fetching articles for top headlines
    #make a list of content to store values on the list
    t_articles = top_headlines['articles']
    articles_results = []
    news = []
    desc = []
    img = []
    p_date = []
    url = []

     #function to fetch all the content
    for i in range(len(t_articles)):
        main_article= t_articles[i]

     #appending list
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        contents = zip(news,desc,img,p_date,url)
        return contents

     #client apikey and id for authorization
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    #all main articles
    all_articles = newsapi.get_everything(sources="bbc-news")
    #fetching all articles of all article news
    a_articles = all_articles['articles']
    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

   

    #function to fetch all the content in everything
    for j in range(len(a_articles)):
        a_articles=a_articles[j]

       
        #appending list all
        news_all.append(a_articles['title'])
        desc_all.append(a_articles['description'])
        img_all.append(a_articles['urlToImage'])
        p_date_all.append(a_articles['publishedAt'])
        url_all.append(a_articles['url'])
        all = zip(news_all,desc_all,img_all,p_date_all,url_all)
        return all

    


