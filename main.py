from fastapi import FastAPI, Request, UploadFile
from fastapi.templating import Jinja2Templates

from utils import tf_idf_map

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.post("/")
async def parse(request: Request, textfile: UploadFile):
    text = await textfile.read()
    words = tf_idf_map(text)

    return templates.TemplateResponse("home.html", {
        "request": request,
        "words": words
    })