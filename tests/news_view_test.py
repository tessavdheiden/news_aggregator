import unittest

from news_view import NewsView


class NewsViewTest(unittest.TestCase):
    def test_has_show_method(self):
        newslist = list()
        newsview = NewsView(newslist)
        newsview.show()

if __name__ == "__main__":
    unittest.main()
