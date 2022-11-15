from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import SessionLocal, engine

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
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_user_item(user_id: int, item:schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=List[schemas.Item])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/services/", response_model=schemas.Service)
def create_service(service:schemas.ServiceCreate, db: Session = Depends(get_db)):
    return crud.create_service(db=db, service=service)

@app.get("/serivces/", response_model=List[schemas.Service])
def get_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_services(db, skip=skip, limit=limit)
    return items

