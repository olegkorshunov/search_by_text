from db import schemas
from db.cruds import crud_post
from fastapi import APIRouter, HTTPException, Query, status, Response
from typing import List

router_post = APIRouter(prefix="/post")


@router_post.get("/", response_model=List[schemas.Post], status_code=status.HTTP_200_OK)
async def read_posts(
    skip: int = 0,
    limit: int = 20,
    search: str = Query(None, max_length=20, description="Search by substring"),
):
    db_posts = await crud_post.get_posts(skip=skip, limit=limit, search=search)
    if not db_posts:
        raise HTTPException(status_code=404, detail="Posts not found")
    return db_posts


@router_post.get(
    "/{post_id}", response_model=schemas.Post, status_code=status.HTTP_200_OK
)
async def read_post(post_id: int):
    db_post = await crud_post.get_post(post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router_post.delete("/{post_id}")
async def delete_post(post_id: int):
    db_post = await crud_post.delete_post(post_id=post_id)
    if db_post == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
