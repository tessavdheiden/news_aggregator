from news_finder import NewsFinder
from news_view import NewsView
from news_parser import NewsParser


def run_news_aggregator():
    newsfinder = NewsFinder("http://127.0.0.1:8080")
    newslist = []
    for page in newsfinder.news_pages():
        p = NewsParser(page)
        news = p.parse()
        newslist.append(news)
    newsview = NewsView(newslist)
    newsview.show()


if __name__ == "__main__":
    run_news_aggregator()


