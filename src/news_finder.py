import requests

class NewsFinder(object):
    def __init__(self, source):
        self.response = None
        self.content = None
        self.search_for_articles(source)

    def news_pages(self):
        if self.content['status'] == 'ok':
            length = len(self.content['articles'])
            for i in range(length):
                yield self.content['articles'][i]

    def exits(self, page):
        if not (page.startswith('http://') or page.startswith('https://')): return False
        self.response = requests.get(page)
        return True if self.response.status_code == 200 else False

    def search_for_articles(self, source):
        # from https://newsapi.org/
        root_url = ('http://newsapi.org/v2/top-headlines?'
               f'sources={source}'
               '&apiKey=2e40f2a1fa0f4d96bc1acbdbef7a3242')

        if self.exits(root_url):
            self.content = self.response.json()




