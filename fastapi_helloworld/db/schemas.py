import datetime
from lib2to3.pytree import Base
from typing import Dict, Optional, Any, List
    
from pydantic import BaseModel

class UpdateField(BaseModel):
    target_field: str
    new_value: Any
    
class TestTBBase(BaseModel):
    test_name: Optional[str] = None
    description: Optional[str] = None

class TestTB(TestTBBase):
    test_id: int