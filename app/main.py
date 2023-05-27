from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2 
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastAPI', user='wootak', password='password', port=5432, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connected!")
        break
    except Exception as error:
        print("Error: ", error)
        time.sleep(4)

my_posts = [{"title:": "title", "content": "content","id": 1}]

def find_post(id):
    for p in my_posts:
        if ["id"] == id:
            return p
@app.get("/")
def get_user():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    posts = cursor.execute("""SELECT * FROM posts""")
    cursor.fetchall()
    print(posts)
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000)
    my_posts.append(post.dic())
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_posts(id: int):

    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
