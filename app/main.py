from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from .database import engine, Base
from .routes import router
from .services.scheduler_agent import start_scheduler


app = FastAPI(title = "AI Marketing Agent")
app.mount("/static", StaticFiles(directory = "app/static"), name = "statis")
app.mount("/generated_images", StaticFiles(directory = "generated_images"), name = "generated_images")

templates = Jinja2Templates(directory = "app/templates")
Base.metadata.create_all(bind = engine)


@app.get("/")
def root():
    return {"message": "Marketing Agent Running"}


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


app.include_router(router)
start_scheduler()
