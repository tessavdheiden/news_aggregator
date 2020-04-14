from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
import markdown
import markdown.extensions.fenced_code
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from src.aggregator import get_news_list


app = FastAPI()
app.mount("/static", StaticFiles(directory="application/static"), name="static")
templates = Jinja2Templates(directory="application/templates")


@app.get("/")
def home():
    readme_file = open('README.md', 'r', encoding='utf-8')
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return HTMLResponse(content=md_template_string, status_code=200)

@app.get("/search")
def get_query():
    with open('application/templates/' + 'input_form.html') as f:
        return HTMLResponse(f.read())


@app.websocket_route("/search/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        query = await websocket.receive_text()
        news_pages = get_news_list(query)
        [await websocket.send_text(f"Article: \"{page.title}\".\t Summary: \"{page.summary}\"") for page in news_pages]


@app.get("/summarize/{query}")
async def get(request: Request, query: str):
    news_pages = get_news_list(query)
    response = templates.TemplateResponse("table.html", {"request": request, "id": 1, "items": news_pages})
    return response

