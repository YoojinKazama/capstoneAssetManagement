from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datatables import DataTable
from sqlalchemy.orm import Session
from routes import asset_route, asset_type_route, asset_provider_route, maintenance_provider_route, maintenance_route, auth_route
from database import get_db
from models import asset_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register template folder
template = Jinja2Templates('templates')

# Mount static folder
app.mount('/static', StaticFiles(directory='static'), name='static')

# Register Routes
app.include_router(auth_route.router)
app.include_router(asset_route.router)
app.include_router(asset_type_route.router)
app.include_router(asset_provider_route.router)
app.include_router(maintenance_provider_route.router)
app.include_router(maintenance_route.router)



@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/login.html", {"request": request})

@app.get("/forbidden", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/forbidden.html", {"request": request})

@app.get("/asset_management/", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/dashboard.html", {"request": request})

@app.get("/asset_management/asset_type", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/asset_type.html", {"request": request})

@app.get("/asset_management/asset_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/asset_provider.html", {"request": request})

@app.get("/asset_management/asset", response_class=HTMLResponse)
def get_asset(request: Request,):
    return template.TemplateResponse("asset_management/admin/asset.html", {"request": request})

@app.get("/asset_management/asset/{id}/view", response_class=HTMLResponse)
def get_asset(request: Request, id: str):
    return template.TemplateResponse("asset_management/admin/asset_view.html", {"request": request, "id": id})
    
