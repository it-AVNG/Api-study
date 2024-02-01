from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_post():
    return {"data": "this is a post"}


@app.post("/create-post")
def create_post(new_post: Post):
    print(new_post)
    return {"data": new_post}


# schema: title str, content str, category, publish bool
