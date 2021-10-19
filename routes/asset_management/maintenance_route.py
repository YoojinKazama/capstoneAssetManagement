  
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from schemas.asset_management.maintenance_schema import CreateMaintenance, UpdateMaintenance
from models.asset_management.maintenance_model import Maintenance
from database import get_db
# from dependencies import get_token


router = APIRouter(
    prefix='/asset_management/api/Maintenance',
    tags=['Maintenance'],
    # dependencies=[Depends(get_token)]
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    maintenance = db.query(Maintenance).filter(Maintenance.active_status == "Active").all()
    return {'data': maintenance}

@router.get('/view/{id}')
def find_one(id: str, db: Session = Depends(get_db)):
    maintenance = db.query(Maintenance).filter(Maintenance.maintenance_id == id).first()
    return {'data': maintenance}

@router.get('/{id}')
def read(id: str, db: Session = Depends(get_db)):
    maintenance = db.query(Maintenance).filter(Maintenance.asset_id == id, Maintenance.active_status == "Active" ).all()
    return {'data': maintenance}


@router.post('/')
def add(maintenance: CreateMaintenance, db: Session = Depends(get_db)):
    try:
        maintenance = Maintenance(

            maintenance_provider_id = maintenance.maintenance_provider_id,
            asset_id = maintenance.asset_id,
            maintenance_name = maintenance.maintenance_name,
            maintenance_details = maintenance.maintenance_details,
            maintenance_cost = maintenance.maintenance_cost,
            maintenance_day = maintenance.maintenance_day,
            maintenance_due = maintenance.maintenance_due,
            maintenance_completed = maintenance.maintenance_completed,
            maintenance_repeatable = maintenance.maintenance_repeatable,
            maintenance_status = maintenance.maintenance_status,


        )
        db.add(maintenance)
        db.commit()
        return {'message': 'asset maintenance created successfully.'}
    except Exception as e:
        print(e)

@router.put('/{id}')
def update(id: str, maintenance: UpdateMaintenance, db: Session = Depends(get_db)): 
    if not db.query(Maintenance).filter(Maintenance.maintenance_id == id).update({
        'maintenance_name': maintenance.maintenance_name,
        'maintenance_details': maintenance.maintenance_details,
        'maintenance_cost': maintenance.maintenance_cost,
        'maintenance_day': maintenance.maintenance_day,
        'maintenance_due': maintenance.maintenance_due,
        'maintenance_completed': maintenance.maintenance_completed,
        'maintenance_repeatable': maintenance.maintenance_repeatable,
        'maintenance_status': maintenance.maintenance_status,
        'remarks': maintenance.remarks,
    }):
        raise HTTPException(404, 'asset provider to update is not found')
    db.commit()
    return {'message': 'asset provider updated successfully.'}

@router.delete('/{id}')
def remove(id: str, db: Session = Depends(get_db)): 
    if not db.query(Maintenance).filter(Maintenance.maintenance_id == id).update({
        'active_status': 'Inactive',
    }):
        raise HTTPException(404, 'asset provider to delete is not found')
    db.commit()
    return {'message': 'asset provider removed successfully.'}