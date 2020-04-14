from src.news_finder import NewsFinder
from src.news_parser import NewsParser


def get_news_list(query: str) -> list:
    newsfinder = NewsFinder(query)
    newslist = []
    for page in newsfinder.news_pages():
        p = NewsParser(page)
        news = p.parse()
        newslist.append(news)
    return newslist





