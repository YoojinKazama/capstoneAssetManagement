from sqlalchemy import Integer, String, Text, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Asset(Base):
    __tablename__ = 'asset'

    asset_id = Column(String(60), primary_key=True)
    # asset_provider_id = Column(String(60), ForeignKey('asset_provider.asset_provider_id'), nullable=True)
    asset_type_id = Column(String(60), ForeignKey('asset_type.asset_type_id'), nullable=True)
    user_id = Column(String(60), ForeignKey('user.user_id'), nullable=True)
    asset_number = Column(Integer, nullable=True)
    asset_cost = Column(Integer, nullable=True)
    asset_name = Column(String(255), nullable=True)
    asset_description = Column(String(255), nullable=True)
    asset_remarks = Column(String(255), nullable=True)
    asset_acquisition = Column(Integer, nullable=True)
    acquisition_date = Column(Integer, nullable=True)
    asset_status = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    # asset_provider = relationship('asset_provider')