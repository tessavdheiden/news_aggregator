import requests

class NewsFinder(object):
    def __init__(self, url):
        self.r = None
        self.urls = list()
        self.get_pages(url)

    def news_pages(self):
        return self.urls

    def exits(self, page):
        if not page.startswith('http://'): return False
        self.r = requests.get(page)
        return True if self.r.status_code == 200 else False

    def get_pages(self, url):
        if self.exits(url + f'/page{0}'):
            self.urls.append(url + f'/page{0}')
