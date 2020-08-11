from flask import Flask, request, jsonify
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
import logging

# initialize sql-alchemy
db = SQLAlchemy()

# local import
from src.summarize import generate_summary
from src.repository import DocumentList

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('errors.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/api/documents/', methods=['GET', 'POST'])
    def create_document():
        """
        This function creates a new document
        """
        if request.method == "POST":
            # Get the person requested
            json_data = request.get_json()
            rawtext = json_data['text']

            try:
                summary = generate_summary(rawtext)
                documentlist = DocumentList(summary=summary, text=rawtext)
                documentlist.save()
                return jsonify(id=documentlist.id), status.HTTP_201_CREATED
            except IndexError as e:
                logger.error('Exception: Text too short')
                return jsonify(error=f"Text too short: {e}"), status.HTTP_411_LENGTH_REQUIRED
            except MemoryError as e:
                logger.error('Too many summaries created')
                return jsonify(error=f'Too many summaries: {e}'), status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
            except Exception as e:
                logger.error('Exception: Server error')
                return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            try:
                results = []
                documentlists = DocumentList.get_all()
                for document in documentlists:
                    obj = {
                        'id': document.id,
                        'text': document.text,
                        'summary': document.summary
                    }
                    results.append(obj)
                return jsonify(results), status.HTTP_200_OK
            except Exception as e:
                logger.error('Exception: Server error')
                return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR

    @app.route('/api/documents/<int:id>', methods=['GET'])
    def document_retrieval(id):
        try:
            document = DocumentList.query.filter_by(id=id).first()
            return jsonify(id=document.id, summary=document.summary), status.HTTP_200_OK
        except Exception as e:
            logger.error('Exception: Server error')
            return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR

    return app


if __name__ == "__main__":
    app = create_app(config_name="production")
    app.run(debug=True)