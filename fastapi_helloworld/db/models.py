from email.policy import default
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Boolean, JSON, ARRAY
from sqlalchemy.sql.functions import current_timestamp

from db.database import Base

class ExampleTable(Base):
    __tablename__ = "example"
    
    test_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="테스트 id"
    )
    
    test_name = Column(
        String(255),
        nullable=True,
        unique=False,
        comment="테스트 이름"
    )
    
    description = Column(
        String(255),
        nullable=True,
        unique=False,
        comment="테스트 설명"
    )