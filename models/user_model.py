from sqlalchemy import Integer, String, Text, DateTime, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(String(36), primary_key=True, default=text('UUID()'))
    user_name = Column(String(255), nullable=True)
    user_email = Column(String(255), nullable=True)
    user_password = Column(String(255), nullable=True)
    user_type = Column(String(255), nullable=True)
    active_status = Column(String(255), nullable=True, default=('Active'))
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    asset = relationship('Asset')
