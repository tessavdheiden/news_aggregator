from flask import Flask, request, jsonify, render_template
from flask_api import status
import logging


from src.document import Document
from src.summarize import generate_summary


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


app = Flask(__name__)

class DocumentRepository(object):
    def __init__(self, capacity):
        self.id = 0
        self.capacity = capacity
        self.document_lst = [Document(id=-1, text="", summary="")]*self.capacity

    def get_id(self):
        ''' Only repository should create ids to prevent creating identical ids '''
        if self.id < self.capacity:
            self.id += 1
            return self.id
        else:
            raise MemoryError

    def add_document(self, id, document: Document):
        self.document_lst[id] = document

    def get_document_from_id(self, id):
        if id < self.capacity:
            return self.document_lst[id]
        else:
            return Document(id=-1, text="", summary="")


repository = DocumentRepository(capacity=10)


@app.route('/api/input', methods=['GET', 'POST'])
def summarize_text():
    json_data = request.get_json()
    rawtext = json_data['text']

    try:
        summary = generate_summary(rawtext)
        id = repository.get_id()
        document = Document(id=id, text=rawtext, summary=summary)
        repository.add_document(id=id, document=document)
        return jsonify(id=id), status.HTTP_201_CREATED
    except IndexError as e:
        logger.error('Exception: Text too short')
        return jsonify(error=f"Text too short: {e}"), status.HTTP_411_LENGTH_REQUIRED
    except MemoryError as e:
        logger.error('Too many summaries created')
        return jsonify(error=f'Too many summaries: {e}'), status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    except Exception as e:
        logger.error('Exception: Server error')
        return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR


@app.route('/api/<id>', methods=['GET'])
def get_summary(id):
    try:
        document = repository.get_document_from_id(int(id))
        return jsonify(id=document.id, summary=document.summary), status.HTTP_200_OK

    except Exception as e:
        logger.error('Exception: Server error')
        return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR


if __name__ == "__main__":
    app.run(debug=True)