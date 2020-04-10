from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import markdown
import markdown.extensions.fenced_code
import uvicorn

from run import run_news_aggregator

app = FastAPI()

@app.get("/")
async def home():
    readme_file = open('README.md', 'r', encoding='utf-8')
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return HTMLResponse(content=md_template_string, status_code=200)

@app.get("/pages/{name}/{index}")
async def update_item(name: str, index: int):
    file = run_news_aggregator(name, index)
    return file

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)