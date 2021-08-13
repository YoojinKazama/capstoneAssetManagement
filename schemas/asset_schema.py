from datetime import datetime as dt
from pydantic import BaseModel

class AssetBase(BaseModel):
    asset_number = int
    asset_cost = int
    asset_name = str
    asset_description = str
    asset_remarks = str
    asset_acquisition = int
    acquisition_date = int
    asset_status = str
    active_status = str


# Schema for request body
class CreateAsset(AssetBase):
    pass

#Schema for response body
class Asset(AssetBase):
    created_at: dt
    updated_at: dt