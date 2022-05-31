import uvicorn
from fastapi import FastAPI

from db.database import database, engine, metadata
from routers.router_post import router_post

metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_post)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
