from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datatables import DataTable
from sqlalchemy.orm import Session
from routes.asset_management import asset_route, asset_type_route, asset_provider_route, maintenance_provider_route, maintenance_route, auth_route, event_route
from routes.asset_management import missing_asset_route, asset_request_route, sell_asset_route, dispose_asset_route, broken_asset_route, repair_asset_route
from routes.asset_management import department_route, maintenance_report_route 
from database import get_db
from models.asset_management import asset_model
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
app.include_router(event_route.router)
app.include_router(missing_asset_route.router)
app.include_router(asset_request_route.router)
app.include_router(sell_asset_route.router)
app.include_router(dispose_asset_route.router)
app.include_router(broken_asset_route.router)
app.include_router(repair_asset_route.router)
app.include_router(department_route.router)
app.include_router(maintenance_report_route.router)


@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/login.html", {"request": request})

@app.get("/index", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/index.html", {"request": request})

@app.get("/forbidden", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/forbidden.html", {"request": request})

@app.get("/asset_management/", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/dashboard.html", {"request": request})

@app.get("/asset_management/requests", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/request_assets.html", {"request": request})

@app.get("/asset_management/asset_type", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/asset_type.html", {"request": request})

@app.get("/asset_management/asset_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/asset_provider.html", {"request": request})

@app.get("/asset_management/asset", response_class=HTMLResponse)
def get_asset(request: Request,):
    return template.TemplateResponse("asset_management/admin/asset.html", {"request": request})

@app.get("/asset_management/asset/view/{id}", response_class=HTMLResponse)
def get_asset(request: Request, id: str):
    return template.TemplateResponse("asset_management/admin/asset_view.html", {"request": request, "id": id})

@app.get("/asset_management/maintenance_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/maintenance_provider.html", {"request": request})

@app.get("/asset_management/maintenance_page", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/admin/maintenance_page.html", {"request": request})

#-------------Equipment Manager----------------#

@app.get("/asset_management/manager", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/dashboard.html", {"request": request})

@app.get("/asset_management/manager/requests", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/request_assets.html", {"request": request})

@app.get("/asset_management/manager/asset_type", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/asset_type.html", {"request": request})

@app.get("/asset_management/manager/asset_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/asset_provider.html", {"request": request})

@app.get("/asset_management/manager/asset", response_class=HTMLResponse)
def get_asset(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/asset.html", {"request": request})

@app.get("/asset_management/manager/asset/view/{id}", response_class=HTMLResponse)
def get_asset(request: Request, id: str):
    return template.TemplateResponse("asset_management/equipment_manager/asset_view.html", {"request": request, "id": id})

@app.get("/asset_management/manager/maintenance_provider", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/maintenance_provider.html", {"request": request})

@app.get("/asset_management/manager/maintenance_page", response_class=HTMLResponse)
def dashboard(request: Request,):
    return template.TemplateResponse("asset_management/equipment_manager/maintenance_page.html", {"request": request})

#-------------USER----------------#

@app.get("/asset_management/user/on_hand_assets", response_class=HTMLResponse)
def get_asset(request: Request,):
    return template.TemplateResponse("asset_management/user/on_hand_assets.html", {"request": request})

@app.get("/asset_management/user/request_assets", response_class=HTMLResponse)
def get_asset(request: Request,):
    return template.TemplateResponse("asset_management/user/request_assets.html", {"request": request})
    
