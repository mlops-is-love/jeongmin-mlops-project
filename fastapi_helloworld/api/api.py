from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Any

from db import cruds, schemas
from db.database import get_db
from api import exceptions
from configurations import APIConfigurations

router = APIRouter()

# === Test Dataset ===

@router.post("/test/create")
def add_test_dataset(
    test_data: schemas.TestTBBase,
    db: Session = Depends(get_db),
    x_token: str = Header(None, title="token")
):
    if x_token != APIConfigurations.header:
        raise exceptions.InvalidHeader(401, f"invalid header")

    return cruds.add_test(
        db=db,
        test_name=test_data.test_name,
        description=test_data.description
    )
    

@router.post("/test/update/{test_id}")
def update_test(
    test_id: int,
    update_field: schemas.UpdateField,
    db: Session = Depends(get_db),
    x_token: str = Header(None, title="token")
):
    if x_token != APIConfigurations.header:
        raise exceptions.InvalidHeader(401, f"invalid header")

    return cruds.update_test(
        db=db,
        update_field=update_field,
        test_id=test_id,
    )

@router.get("/test/get/all")
def test_all(
    db: Session = Depends(get_db),
    x_token: str = Header(None, title="token")
):
    if x_token != APIConfigurations.header:
        raise exceptions.InvalidHeader(401, f"invalid header")

    return cruds.select_test_all(db=db)


@router.get("/test/get/{test_id}")
def test_by_id(
    test_id: int, 
    db: Session = Depends(get_db),
    x_token: str = Header(None, title="token")
):
    if x_token != APIConfigurations.header:
        raise exceptions.InvalidHeader(401, f"invalid header")

    return cruds.select_test_by_id(db=db, test_id=test_id)

