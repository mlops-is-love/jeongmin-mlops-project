from typing import Optional, Dict, List, Any
from sqlalchemy.orm import Session

from db import models
from db import schemas
from api import exceptions

def add_test(
    db: Session,
    test_name: Optional[str] = None,
    description: Optional[str] = None,
) -> schemas.TestTB:
    test_data = models.TestDataset(
        test_name=test_name,
        description=description, 
    )
    db.add(test_data)
    db.commit()
    db.refresh(test_data)
    
    return test_data


def update_test(
    db: Session,
    test_id: int,
    update_field: schemas.UpdateField,
) -> schemas.TestTB:
    test_data = select_test_by_id(
        db=db,
        test_id=test_id,
    )
    
    if update_field.target_field == "test_name":
        test_data.test_name = update_field.new_value
    elif update_field.target_field == "description":
        test_data.description = update_field.new_value
    else:
        # TODO: Exception handling
        pass
    
    db.commit()
    db.refresh(test_data)
    return test_data


def select_test_all(db: Session) -> List[schemas.TestTB]:
    return db.query(models.ExampleTable).all()


def select_test_by_id(
    db: Session,
    test_id: int,
) -> schemas.TestTB:
    result = db.query(models.ExampleTable).filter(models.ExampleTable.test_id == test_id).first()

    if result == None:
        raise exceptions.NotExist(400, f"test_id('{test_id}') does not exist in ExampleTable table")
    
    return result

