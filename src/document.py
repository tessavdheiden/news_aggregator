import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='document.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class Document(object):
    def __init__(self, id: int, text: str, summary: str):
        self.id = id
        self.text = text
        self.summary = summary

        logger.info(f'Created document {self.id}')
