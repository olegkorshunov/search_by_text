from db import schemas
from db.cruds import crud_post
from fastapi import APIRouter, HTTPException, status

router_post = APIRouter(prefix="/post")


@router_post.get(
    "/{post_id}", response_model=schemas.Post, status_code=status.HTTP_200_OK
)
async def read_post(post_id: int):
    db_post = await crud_post.get_post(post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
