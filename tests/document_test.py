import unittest

from src.document import Document


class NewsTest(unittest.TestCase):
    def test_summary(self):
        d = Document(id=1, summary="foo", text="bar")
        self.assertEqual(d.summary, "foo")
        self.assertEqual(d.text, "bar")
        self.assertEqual(d.id, 1)

if __name__ == "__main__":
    unittest.main()