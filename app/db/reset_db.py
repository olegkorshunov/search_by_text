import os
import sqlite3

import pandas as pd

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))


def resetDB():
    df = pd.read_csv(os.path.join(BASE_FOLDER, "posts.csv"))
    df.created_date = df.created_date.astype("datetime64")
    conn = sqlite3.connect(os.path.join(BASE_FOLDER, "posts.sqlite"))
    df.to_sql("posts", con=conn, if_exists="replace", index_label="id")
    conn.close()
    print("DB is resetting successed!")


if __name__ == "__main__":
    resetDB()
