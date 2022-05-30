from typing import List
from fastapi import FastAPI, HTTPException
from db.database import database, engine, metadata
from db.cruds import crud_post
import uvicorn
from db import schemas

# import crud
# import schemas


metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/post/{post_id}")  # , response_model=schemas.Post)
async def read_user(post_id: int):
    db_post = await crud_post.get_post(post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
