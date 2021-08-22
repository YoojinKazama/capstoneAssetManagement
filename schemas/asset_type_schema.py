from datetime import datetime as dt
from pydantic import BaseModel

class AssetTypeBase(BaseModel):
    asset_type_title: str


# Schema for request body
class CreateAssetType(AssetTypeBase):
    asset_type_title: str
    description: str

#Schema for response body
class Asset(AssetTypeBase):
    created_at: dt
    updated_at: dt

    