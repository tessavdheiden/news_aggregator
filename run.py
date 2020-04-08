from src.news_finder import NewsFinder
from src.news_view import NewsView
from src.news_parser import NewsParser


def run_news_aggregator():
    newsfinder = NewsFinder("bbc-news")
    newslist = []
    for page in newsfinder.news_pages():
        p = NewsParser(page)
        news = p.parse()
        newslist.append(news)
    newsview = NewsView(newslist)
    newsview.show()


if __name__ == "__main__":
    run_news_aggregator()


