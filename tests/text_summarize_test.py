import unittest

from src.summarize import generate_summary


class TextSummarizeTest(unittest.TestCase):
    def test_sumy_summarize(self):
        with open("example_text.txt", "r", encoding="utf-8") as f:
            raw_text=f.readline()
            summary = generate_summary(raw_text)
            self.assertIsInstance(summary, str)
            self.assertNotEqual(len(summary), len(raw_text))

if __name__ == "__main__":
    unittest.main()
