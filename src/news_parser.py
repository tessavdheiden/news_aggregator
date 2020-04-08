from src.news import News

class NewsParser(object):
    def __init__(self, page):
        self.page = page
        self.text = ""
        self.summary = ""
        self.set_text()
        self.set_summary()

    def parse(self):
        return News(text=self.text, summary=self.summary)

    def set_text(self):
        self.text = self.page['content']

    def set_summary(self):
        self.summary = self.page['description']

