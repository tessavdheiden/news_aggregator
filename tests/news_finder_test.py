import unittest

from news_finder import NewsFinder


class NewsFinderTest(unittest.TestCase):
    def test_page_method_returns_iterable(self):
        newsfinder = NewsFinder("fakeurl")
        self.assertIsInstance(newsfinder.news_pages(), list)

    def test_get_1_page(self):
        newsfinder = NewsFinder("http://127.0.0.1:8080")
        self.assertEqual(len(newsfinder.news_pages()), 1)


if __name__ == "__main__":
    unittest.main()