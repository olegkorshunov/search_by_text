from db.database import metadata
from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),  # , index=True),
    Column("text", String, nullable=False),
    Column("created_date", TIMESTAMP(timezone=True), nullable=False),
    Column("rubrics", String, nullable=False),
)
