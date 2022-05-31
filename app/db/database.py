import os

import databases
from sqlalchemy import MetaData, create_engine

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
DB_NAME = "posts.sqlite"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_FOLDER,DB_NAME)}"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata = MetaData()
