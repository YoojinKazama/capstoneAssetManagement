  
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from schemas.asset_management.maintenance_report_schema import CreateReport
from models.asset_management.maintenance_report_model import Maintenance_Report
from database import get_db
# from dependencies import get_token


router = APIRouter(
    prefix='/asset_management/api/Maintenance_report',
    tags=['Maintenance_report'],
    # dependencies=[Depends(get_token)]
)

@router.get('/')
def read(db: Session = Depends(get_db)):
    report = db.query(Maintenance_Report).all()
    if not report:
        raise HTTPException(404, 'reports not found')
    return {'data': report}

@router.post('/')
def add(report: CreateReport, db: Session = Depends(get_db)):
    try:
        report_details = Maintenance_Report(
            
            maintenance_id = report.maintenance_id,
            maintenance_cost = report.maintenance_cost,
            completed_date = report.completed_date,

        )
        db.add(report_details)
        db.commit()
        return {'message': 'report created successfully.'}
    except Exception as e:
        print(e)