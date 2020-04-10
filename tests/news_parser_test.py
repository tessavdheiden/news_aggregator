import unittest

from src.news_parser import NewsParser
from src.news import News


class NewsParserTest(unittest.TestCase):
    def test_input_dict(self):
        page = "fake"
        newsparser = NewsParser(page)
        self.assertEqual(newsparser.text, "")

        page = {"description":"foo","content":"bar"}
        newsparser = NewsParser(page)
        self.assertEqual(newsparser.text, "bar")

    def test_parse(self):
        page = {"description":"foo","content":"bar"}
        newsparser = NewsParser(page)
        news = newsparser.parse()
        self.assertIsInstance(news, News)

if __name__ == "__main__":
    unittest.main()
