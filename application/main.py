from flask import Flask, request, jsonify, render_template
from flask_api import status
import logging


from src.document import Document
from src.summarize import generate_summary


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
        return jsonify(error=f"Text too short: {e}"), status.HTTP_411_LENGTH_REQUIRED
    except Exception as e:
        return jsonify(error=f"Unable to generate summary: {e}"), status.HTTP_500_INTERNAL_SERVER_ERROR



if __name__ == "__main__":
    app.run(debug=True)