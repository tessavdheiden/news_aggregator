import unittest

from src.summarize import nltk_summarizer, get_word_freq_dict


class NewsFinderTest(unittest.TestCase):
    def test_get_word_freq_dict(self):
        self.assertEqual(1, 1)
        source = 'fake'
        newsfinder = NewsFinder(source)
        self.assertIsInstance(newsfinder.news_pages(), dict)

    def test_get_cnn_article(self):
        source = 'cnn'
        newsfinder = NewsFinder(source)
        page = next(newsfinder.news_pages())
        self.assertIsInstance(page, dict)

    def test_get_distinct_techcrunch_articles(self):
        source = 'techcrunch'
        newsfinder = NewsFinder(source)
        pages = []
        for i, page in enumerate(newsfinder.news_pages()):
            pages.append(page)
            if i == 1:
                break
        self.assertNotEqual(pages[0], pages[1])



if __name__ == "__main__":
    unittest.main()