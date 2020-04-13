class NewsView(object):
    def __init__(self, newslist):
        self.newslist = newslist

    def show(self, i):
        data = {}
        data['document_id'] = i
        data['summary'] = self.newslist[i].summary
        return data


