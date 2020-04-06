import unittest

from news import News


class NewsTest(unittest.TestCase):
    def test_summary(self):
        news = News(summary="foo", text="bar")
        self.assertEqual(news.summary, "foo")
        self.assertEqual(news.text, "bar")

if __name__ == "__main__":
    unittest.main()