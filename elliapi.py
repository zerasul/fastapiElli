from fastapi import FastAPI,Response,Request
from os import listdir,environ
from random import randint
app = FastAPI()


@app.get("/api/gif")
def get_random_gif(request=Request):
    files = listdir("images/")
    id= randint(0,len(files))
    domain= "localhost:8000"
    if 'MY_DOMAIN' in environ:
        domain=environ['MY_DOMAIN']
    return {"id": id,"url":f'https://{domain}/api/gif/{id}.gif'}

@app.get("/api/gif/{id}.gif")
def get_gif(id:int):

    return Response(content=readFile(id),media_type="image/gif")

def readFile(id:int):
    with open(f'images/{id}.gif', mode='rb') as file:
        return file.read()
