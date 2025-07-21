from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.OrderOut)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)


@router.get("/{order_id}", response_model=schemas.OrderOut)
def read_order(order_id: int, db: Session = Depends(get_db)):
    return crud.get_order(db, order_id)


@router.put("/{order_id}", response_model=schemas.OrderOut)
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return crud.update_order(db, order_id, order)
