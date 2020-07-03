from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
# from starlette.requests import Request
# from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "hello": "hello"})


@app.get("/{hello}")
async def main(request: Request, hello: str):
    return templates.TemplateResponse("index.html", {"request": request, "hello": hello})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
