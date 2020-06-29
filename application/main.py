from flask import Flask, request, jsonify, render_template
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
    except IndexError as e:
        print("Text too short ")
        summary = ""
    except Exception as e:
        print("Exception: ", e)
        summary = ""
    finally:
        document = Document(id=len(document_list), text=rawtext, summary=summary)
        document_list.append(document)
        status = 'error' if summary == "" else 'success'

    return jsonify(text=rawtext, summary=summary, status=status)


if __name__ == "__main__":
    app.run(debug=True)