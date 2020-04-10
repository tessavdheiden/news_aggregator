import json


class NewsView(object):
    def __init__(self, newslist):
        self.newslist = newslist
    #
    # def save_json(self, newslist, i):
    #     for i, news in enumerate(newslist):
    #         with open(f'./data/{i}.txt', 'w') as outfile:
    #             data = {}
    #             data['document_id'] = i
    #             data['summary'] = newslist[i].summary
    #             json.dump(data, outfile)

    def show(self, i):
        data = {}
        data['document_id'] = i
        data['summary'] = self.newslist[i].summary
        return data


