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




class DocumentRepository(object):
    def __init__(self, capacity):
        self.id = 0
        self.capacity = capacity
        self.document_lst = [Document(id=-1, text="", summary="")]*self.capacity

    def get_id(self):
        """
        Only repository should create ids to prevent creating identical ids
        """
        if self.id < self.capacity:
            self.id += 1
            return self.id
        else:
            raise MemoryError

    def add_document(self, document: Document):
        self.document_lst[document.id] = document

    def get_document_from_id(self, id):
        if id < self.capacity:
            return self.document_lst[id]
        else:
            return Document(id=-1, text="", summary="")


repository = DocumentRepository(capacity=10)

def create_app():
    app = Flask(__name__)

    @app.route('/api/document', methods=['GET', 'POST'])
    def create_document():
        """
        This function creates a new document
        TODO: cleaner: https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way
        """
        # Get the person requested
        json_data = request.get_json()
        rawtext = json_data['text']

        try:
            summary = generate_summary(rawtext)
            id = repository.get_id()
            document = Document(id=id, text=rawtext, summary=summary)
            repository.add_document(document=document)
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


    @app.route('/api/document/<int:id>', methods=['GET'])
    def get_summary(id):
        """
        This function returns a summary of a document by id
        """
        try:
            document = repository.get_document_from_id(int(id))
            return jsonify(id=document.id, summary=document.summary), status.HTTP_200_OK

        except Exception as e:
            logger.error('Exception: Server error')
            return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)