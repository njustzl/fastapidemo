from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sys
sys.path.append('.')

from contact import crud, models, schemas
from contact.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_phone(db, phone=user.phone)
    if db_user:
        raise HTTPException(status_code=400, detail="Phone no. already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/", response_model=schemas.User)
def update_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user=user)


# @app.delete("/users/", response_model=schemas.User)
# def delete_user(user: schemas.User, db: Session = Depends(get_db)):
#     return crud.delete_user(db=db, user=user)


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user_by_id(db=db, user_id=user_id)
