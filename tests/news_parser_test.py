import unittest

from news_parser import NewsParser
from news import News


class NewsParserTest(unittest.TestCase):
    def test_parse(self):
        page = "http://127.0.0.1:8080/page0" # TODO: catch "fakeurl"
        newsparser = NewsParser(page)
        news = newsparser.parse()
        self.assertIsInstance(news, News)


if __name__ == "__main__":
    unittest.main()
