from datetime import datetime as dt
from pydantic import BaseModel

class AssetBase(BaseModel):
    asset_provider_id : str
    asset_type_id : str
    # user_id : str
    # department_id : str
    # asset_number : int
    asset_cost : int
    asset_title : str
    asset_description : str
    asset_brand : str
    asset_model : str
    asset_serial : str
    asset_acquisition : str
    acquisition_date : dt
    # asset_status : str


# Schema for request body
class CreateAsset(AssetBase):
    pass

class UpdateAsset(AssetBase):
    asset_status: str
    

#Schema for response body
class Asset(AssetBase):
    created_at: dt
    updated_at: dt