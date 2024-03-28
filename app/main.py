from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from . import models
from .database import engine
from .config import settings

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

"""
import psycopg2
import time
from typing import List
from fastapi import FastAPI, status, Response, HTTPException, Depends
from psycopg2.extras import RealDictCursor
from app import utils
from . import models, schema, utils
from .database import engine, get_db
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="CvaD12345",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Database connection failed!")
        print("Error: ", error)
        time.sleep(2)


@app.get("/posts")
def get_posts():
    cursor.execute(SELECT * FROM posts)
    posts = cursor.fetchall()
    return {"Data": posts}


@app.get("/posts/latest")
def get_latest_post():
    cursor.execute(SELECT * FROM posts ORDER BY id DESC LIMIT 1)
    post = cursor.fetchone()
    return {"Detail": post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(SELECT * FROM posts WHERE id = %s, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} doesn't exist",
        )
    return {"Post": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute(
        INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *,
        (post.title, post.content, post.published),
    )
    post = cursor.fetchone()
    conn.commit()
    return {"Data": post}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *,
        (post.title, post.content, post.published, str(id)),
    )
    post = cursor.fetchone()
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} doesn't exist",
        )
    conn.commit()
    return {"Data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(DELETE FROM posts WHERE id = %s RETURNING *, (str(id),))
    post = cursor.fetchone()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} doesn't exist",
        )
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
 """
