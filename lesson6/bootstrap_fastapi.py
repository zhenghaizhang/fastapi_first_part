from fastapi.requests import Request
from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/user/")
async def files(
                    request: Request,
                    username: str = Form(...),
                    password: str = Form(...),
                ):
    print('username ', username)
    print('password ', password)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "username": username,
        }
    )


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
