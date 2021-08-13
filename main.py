from fastapi import FastAPI, Request, Depends
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from sqlalchemy.orm import Session
from routes import asset_route
from routes import asset_type_route
from database import get_db


app = FastAPI()


# Register Routes
# app.include_router(authRoutes.router)
app.include_router(asset_route.router)
app.include_router(asset_type_route.router)
