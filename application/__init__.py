from fastapi import FastAPI
import json
import os, os.path
from fastapi.responses import HTMLResponse
import markdown
import markdown.extensions.fenced_code

app = FastAPI()

@app.get("/")
def home():
    readme_file = open('README.md', 'r', encoding='utf-8')
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return HTMLResponse(content=md_template_string, status_code=200)

@app.get("/instructions")
def root():
    count = len([name for name in os.listdir('.') if os.path.isfile(name)])
    return f"Select news file: 0-{count}"


@app.get("/pages/{item_id}")
def read_item(item_id: int):
    with open(f"data/{item_id}.txt", 'r') as f:
        file = json.load(f)
    return file