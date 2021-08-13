from sqlalchemy import Integer, String, Text, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import uuid


class Asset_Type(Base):
    __tablename__ = 'asset_type'

    asset_type_id = Column(String(36), primary_key=True, default=text('UUID()'))
    asset_type_name = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, default=('is_active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))