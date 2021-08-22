from datetime import datetime as dt
from pydantic import BaseModel

class MaintenanceBase(BaseModel):
    maintenance_provider_id: str
    asset_id: str
    maintenance_name: str
    maintenance_cost: int
    maintenance_day: int
    maintenance_due: dt
    maintenance_status: str
    remarks: str


# Schema for request body
class CreateMaintenance(MaintenanceBase):
    pass

class UpdateBase(BaseModel):
    maintenance_provider_id: str
    maintenance_name: str
    maintenance_cost: int
    maintenance_day: int
    maintenance_due: dt
    maintenance_status: str
    remarks: str

class UpdateMaintenance(UpdateBase):
    pass


#Schema for response body
class Asset(MaintenanceBase):
    created_at: dt
    updated_at: dt