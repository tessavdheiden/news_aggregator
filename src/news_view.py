from application import app
import uvicorn
import json

class NewsView(object):
    def __init__(self, newslist):
        self.save_json(newslist)

    def save_json(self, newslist):
        for i, news in enumerate(newslist):
            with open(f'./data/{i}.txt', 'w') as outfile:
                data = {}
                data['document_id'] = i
                data['summary'] = news.summary
                json.dump(data, outfile)

    def show(self):
        uvicorn.run(app)
