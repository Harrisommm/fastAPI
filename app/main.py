from fastapi import FastAPI
import psycopg2 
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Hello World"}