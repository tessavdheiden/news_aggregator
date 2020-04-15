from flask import Flask, request, jsonify, render_template
from src.document import Document
from src.summarize import nltk_summarizer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

document_list = []

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    rawtext = request.form['rawtext']
    summary = nltk_summarizer(rawtext)
    document = Document(id=len(document_list), text=rawtext, summary=summary)
    document_list.append(document)
    return render_template('index.html', items=document_list, result=len(document_list))


@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)