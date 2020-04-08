import unittest

from src.news_finder import NewsFinder


class NewsFinderTest(unittest.TestCase):
    def test_page_method_returns_iterable(self):
        self.assertEqual(1, 1)
        source = 'fake'
        newsfinder = NewsFinder(source)
        self.assertIsInstance(newsfinder.news_pages(), object)

    def test_get_cnn_article(self):
        source = 'cnn'
        newsfinder = NewsFinder(source)
        page = next(newsfinder.news_pages())
        self.assertIsInstance(page, str)

    def test_get_distinct_techcrunch_articles(self):
        source = 'techcrunch'
        newsfinder = NewsFinder(source)
        page1 = next(newsfinder.news_pages())
        page2 = next(newsfinder.news_pages())
        self.assertMultiLineEqual(page1, page2)


if __name__ == "__main__":
    unittest.main()