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

document_list = []


@app.route('/api/input', methods=['GET', 'POST'])
def summarize_text():
    json_data = request.get_json()
    rawtext = json_data['text']

    try:
        summary = generate_summary(rawtext)
        document = Document(id=len(document_list), text=rawtext, summary=summary)
        document_list.append(document)
        return jsonify(text=rawtext, summary=summary)
    except IndexError as e:
        logger.error('Exception: Text too short')
        return jsonify(error=f"Text too short: {e}"), status.HTTP_411_LENGTH_REQUIRED
    except Exception as e:
        logger.error('Exception: Server error')
        return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR



if __name__ == "__main__":
    app.run(debug=True)