from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone == phone).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        # image=user.image,
        email=user.email,
        # birthday=user.birthday,
        phone=user.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.User):
    if user.id is None:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    db_user = get_user(db, user.id)
    if db_user is None:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    db_user.name = user.name
    # db_user.image = user.image
    db_user.email = user.email
    # db_user.birthday = user.birthday
    db_user.phone = user.phone
    db.add(db_user)
    db.commit()
    return db_user


def delete_user(db: Session, user: schemas.User):
    if user.id is None:
        return None
    db_user = get_user(db, user.id)
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    if user_id is None:
        return None
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
