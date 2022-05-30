from db.database import database
from db.models.post import posts


async def get_post(post_id: int):
    post = dict(await database.fetch_one(posts.select().where(posts.c.id == post_id)))
    return post
