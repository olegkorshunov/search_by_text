from typing import Optional

from db.database import database
from db.models.post import posts


async def get_posts(skip: int = 0, limit: int = 20, search: Optional[str] = None):
    if search:
        query = (
            posts.select()
            .filter(posts.c.text.contains(search))
            .offset(skip)
            .limit(limit)
        )
        results = await database.fetch_all(query)
    else:
        results = await database.fetch_all(posts.select().offset(skip).limit(limit))
    return [dict(result) for result in results]


async def get_post(post_id: int):
    post = dict(await database.fetch_one(posts.select().where(posts.c.id == post_id)))
    return post


async def delete_post(post_id: int):
    query = posts.delete().where(posts.c.id == post_id)
    result = await database.execute(query)
    print(result)
    return result
