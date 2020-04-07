import requests

from news import News

class NewsParser(object):
    def __init__(self, page):
        self.r = requests.get(page)
        self.text = self.get_text()
        self.summary = None

    def parse(self):
        return News(text=self.text, summary=self.summary)

    def get_text(self):
        return self.r.json()['page']['text']
