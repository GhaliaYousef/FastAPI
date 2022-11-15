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
# MONGO_DETAILS = "mongodb+srv://ghalia:826555666@fasterapi.brzllhb.mongodb.net/?retryWrites=true&w=majority"
# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# database = client.FASTAPI
# FASTAPI_collection = database.get_collection("ghalia")

# def schema_helper(data) -> dict:
#     '''
#     helper to make the mongo query into dict form
#     '''
#     return {
#         "id": str(data["_id"]),
#         "SKU": data["sku"],
#         "Brand Name": data["brand_name"],
#         "Title": data["title"],
#         "Thumbnail":  data["thumbnail"],
#         "Available Price":  data["available_price"],
#         "MRP":  data["mrp"]
#     }


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# Retrieve all datas present in the database
# @app.get("/")
# async def get_all_data():
#     datas = []
#     async for data in FASTAPI_collection.find():
#         datas.append(schema_helper(data))
#     return datas

# Retrieve a data with a matching ID present in the database
# @app.get("/{data_id}")
# async def get_data(data_id:str):
#     data_data = await FASTAPI_collection.find_one({"_id": ObjectId(data_id)})
#     return schema_helper(data_data)

# Add a new data into to the database
# @app.post('/new/')
# async def post_data(item: dict) -> dict:
#     data_data = await FASTAPI_collection.insert_one(item)
#     new_data = await FASTAPI_collection.find_one({"_id": data_data.inserted_id})
#     return schema_helper(new_data)


# Delete a data from the database
# @app.delete('/delete_data/{data_id}')
# async def delete_data(data_id: str):
#     '''
#     Return: 
#             true, once the data got deleted.
#     '''
#     data = await FASTAPI_collection.find_one({"_id": ObjectId(data_id)})
#     if data:
#         await FASTAPI_collection.delete_one({"_id": ObjectId(data_id)})
#         return True
#     return False

# Update data with a matching ID
# @app.put('/update_data/{data_id}')
# async def update_data(id: str, data: dict):
#     '''
#     Return: 
#             true, once the data element got updated.
#             false, if an empty request body is sent.
#     '''
#     if len(data) < 1:
#         return False
#     data = await FASTAPI_collection.find_one({"_id": ObjectId(id)})

#     #add update and update time field to get tracked
#     data.update({"update":True, "updated_time":datetime.now()})
#     if data:
#         updated_data = await FASTAPI_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_data:
#             return True
#         return False
# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}

# @app.get("/items/{item_id1}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         taxed_price = item.price + item.tax
#         item_dict.update({"Prices after tax":taxed_price})
#     return item_dict

