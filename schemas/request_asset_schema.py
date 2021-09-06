from typing import Optional
from datetime import datetime as dt
from pydantic import BaseModel

class RequestBase(BaseModel):
    asset_type_id: str
    request_brand: str
    request_model: str
    request_description: str
    
    


# Schema for request body
class CreateRequest(RequestBase):
    request_status: str
    created_by: str
    

class UpdateStatusRequest(BaseModel):
    request_status: str
    request_remark: str
    updated_by: str