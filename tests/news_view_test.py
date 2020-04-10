import unittest

from src.news_view import NewsView
from src.news import News

class NewsViewTest(unittest.TestCase):
    def test_save_json(self):
        newslist = [News("foo", "bar")]
        newsview = NewsView(newslist)


if __name__ == "__main__":
    unittest.main()
