import unittest

from news_finder import NewsFinder


class NewsFinderTest(unittest.TestCase):
    def test_page_method_returns_iterable(self):
        newsfinder = NewsFinder("fakeurl")
        self.assertIsInstance(newsfinder.news_pages(), list)

if __name__ == "__main__":
    unittest.main()
