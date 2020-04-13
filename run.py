from src.news_finder import NewsFinder
from src.news_parser import NewsParser


def get_news_list(news_source="bbc-news", index=1): # get_news_list(source)
    newsfinder = NewsFinder(news_source)
    newslist = []
    for page in newsfinder.news_pages():
        p = NewsParser(page)
        news = p.parse()
        newslist.append(news)
    return newslist

#def get_news(url):





