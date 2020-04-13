from fastapi import FastAPI, Request, Form, WebSocket, Depends, Cookie, Header, status
from fastapi.responses import HTMLResponse, FileResponse
import markdown
import markdown.extensions.fenced_code
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from run import get_news_list


app = FastAPI()
app.mount("/static", StaticFiles(directory="application/static"), name="static")
templates = Jinja2Templates(directory="application/templates")


@app.get("/")
async def home():
    readme_file = open('README.md', 'r', encoding='utf-8')
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return HTMLResponse(content=md_template_string, status_code=200)

@app.get("/search")
async def get():
    with open('application/templates/' + 'input_form.html') as f:
        return HTMLResponse(f.read())


@app.websocket_route("/search/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        news_pages = get_news_list(data)
        [await websocket.send_text(f"Article: \"{page.title}\".\t Summary: \"{page.summary}\"") for page in news_pages]


@app.get("/sources/{source}")
async def get_source(request: Request, source: str):
    news_pages = get_news_list(source)
    return templates.TemplateResponse("table.html", {"request": request, "id": source, "items": news_pages})


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)