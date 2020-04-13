from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from run import get_news_list
#from run import get_news

#app = FastAPI()
from application import app

app.mount("/static", StaticFiles(directory="static"), name="static")


class Item(object):
    name: str
    summary: str

item = Item()
item.title = "Tessa"
item.summary = "van der Heiden"
items = [item] + [item]

templates = Jinja2Templates(directory="templates")


@app.get("/{id}")
async def home(request: Request, id: str):
    news_pages = get_news_list(id)
    #news_pages = items
    return templates.TemplateResponse("homepage.html", {"request": request, "id": id, "items": news_pages})

@app.post("/files")
async def create_file(request: Request):
     form: FormData = await request.form()
     files = form.getlist("files")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)