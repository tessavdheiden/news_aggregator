import unittest

from src.news_view import NewsView


class NewsViewTest(unittest.TestCase):
    def test_save_json(self):
        newslist = list(News("foo", "bar"))
        newsview = NewsView(newslist)


if __name__ == "__main__":
    unittest.main()
