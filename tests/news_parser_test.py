import unittest

from src.news_parser import NewsParser
from src.news import News


class NewsParserTest(unittest.TestCase):
    def test_url_valid(self):
        page = "fake"
        newsparser = NewsParser(page)
        self.assertFalse(newsparser.exits())

        page = "https://thenextweb.com/hardfork/2020/04/08/satoshi-nakaboto-bitcoin-correlates-with-sp-500-during-coronavirus-pandemic/"
        newsparser = NewsParser(page)
        self.assertTrue(newsparser.exits())

    def test_parse(self):
        page = "https://thenextweb.com/hardfork/2020/04/08/satoshi-nakaboto-bitcoin-correlates-with-sp-500-during-coronavirus-pandemic/"
        newsparser = NewsParser(page)
        news = newsparser.parse()
        self.assertIsInstance(news, News)

    def test_parse_news_object_content(self):
        page = "https://www.bbc.com/news/entertainment-arts-52212571"
        newsparser = NewsParser(page)
        news = newsparser.parse()
        self.assertIsInstance(news.text, str)

if __name__ == "__main__":
    unittest.main()
