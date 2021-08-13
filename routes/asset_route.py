  
from fastapi import APIRouter, Depends, HTTPException, Cookie
from sqlalchemy.orm import Session
from schemas.asset_schema import CreateAsset
from models.asset_model import Asset
from database import get_db
# from dependencies import get_token


router = APIRouter(
    prefix='/asset',
    tags=['asset'],
    # dependencies=[Depends(get_token)]
)

@router.get('/')
def all(db: Session = Depends(get_db)):
    asset = db.query(Asset).all()
    return {'data': asset}

@router.get('/{id}')
def read(id: int, db: Session = Depends(get_db)):
    asset = db.query(Asset).filter(Asset.id == id).first()
    if not asset:
        raise HTTPException(404, 'asset not found')
    return {'data': asset}

@router.post('/add_Asset')
def add_asset(request: CreateAsset, db: Session = Depends(get_db)):
    try:
        asset = Asset(
            asset_description = request.asset_description,
            # age = request.age,
            # password = request.password
        )
        db.add(asset)
        db.commit()
        return {'message': 'Created a new Asset'}
    except Exception as e:
        print(e)

# @router.put('/{id}')
# def update(id: int, asset: CreateUser, db: Session = Depends(get_db)): 
#     if not db.query(asset).filter(asset.id == id).update({
#         'name': asset.name,
#         'age': asset.age
#     }):
#         raise HTTPException(404, 'asset to update is not found')
#     db.commit()
#     return {'message': 'asset updated successfully.'}

# @router.delete('/{id}')
# def remove(id: int, db: Session = Depends(get_db)):
#     if not db.query(asset).filter(asset.id == id).delete():
#         raise HTTPException(404, 'asset to delete is not found')
#     db.commit()
#     return {'message': 'asset removed successfully.'}