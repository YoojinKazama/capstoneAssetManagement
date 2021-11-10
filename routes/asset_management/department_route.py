from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database import get_db
from models.asset_management.department_model import Department
from schemas.asset_management.department_schema import CreateDepartment

router = APIRouter(
    prefix='/asset_management/api/Department',
    tags=['Department']
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    department = db.query(Department).all()
    return {'data': department}

@router.post('/')
def add(department: CreateDepartment, db: Session = Depends(get_db)):
    try:
        department_schema = Department(
            
            department_name = department.department_name,
        )

        db.add(department_schema)
        db.commit()
        return {'message': 'department created successfully.'}
    except Exception as e:
        print(e)