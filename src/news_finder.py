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
                if self.content['articles'][i]['description']: # can be None
                    yield self.content['articles'][i]

    def exits(self):
        return True if self.response.status_code == 200 else False

    def search_for_articles(self, source):
        url = 'https://newsapi.org/v2/everything?'
        parameters = {
            'q': source,  # query phrase
            'pageSize': 10,  # maximum is 100
            'apiKey': '2e40f2a1fa0f4d96bc1acbdbef7a3242'  # your own API key
        }
        self.response = requests.get(url, params=parameters)

        if self.exits():
            self.content = self.response.json()




