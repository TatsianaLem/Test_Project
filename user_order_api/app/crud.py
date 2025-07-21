from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas



def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db_user.name = user.name
    db_user.age = user.age
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(db: Session, user_id: int, updates: schemas.UserUpdate):
    user = get_user(db, user_id)
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(user, field, value)
    db.commit()
    db.refresh(user)
    return user



def create_order(db: Session, order: schemas.OrderCreate):
    user = db.query(models.User).filter(models.User.id == order.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_order = models.Order(
        title=order.title,
        description=order.description,
        user_id=order.user_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_id: int):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


def update_order(db: Session, order_id: int, updates: schemas.OrderUpdate):
    order = get_order(db, order_id)
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(order, field, value)
    db.commit()
    db.refresh(order)
    return order
