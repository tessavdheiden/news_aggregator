from src.news import News

class NewsParser(object):
    def __init__(self, page):
        self.text = ""
        self.summary = ""
        self.title = ""
        if isinstance(page, dict):
            self.page = page
            self.set_fields()
    def parse(self):
        return News(title=self.title, text=self.text, summary=self.summary)

    def set_fields(self):
        self.title = self.page['title']
        self.text = self.page['content']
        self.summary = self.page['description']

# TODO: Better to instantiate a News object and set the fields in the methods?