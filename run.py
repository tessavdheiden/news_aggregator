from src.news_finder import NewsFinder
from src.news_view import NewsView
from src.news_parser import NewsParser


def run_news_aggregator(news_source="bbc-news", index=1):
    newsfinder = NewsFinder(news_source)
    newslist = []
    for page in newsfinder.news_pages():
        p = NewsParser(page)
        news = p.parse()
        newslist.append(news)
    newsview = NewsView(newslist)
    return newsview.show(index)


if __name__ == "__main__":
    run_news_aggregator()


