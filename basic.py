from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_route():
    return {'msg':'Devashish'}



"""
# ----------------------------------------------------------
# Path parameter
@app.get('/greet/{name}')
async def greet_name_path(name:str) -> dict:
    return {'msg':f'Hello {name}'}
# http://127.0.0.1:8000/greet/dev

# Query parameter
@app.get('/greet1')
async def greet_name_query(name:str):
    return f'Hello {name}'
# http://127.0.0.1:8000/greet1?name=dev

# Both Path and Query parameter
@app.get('/greet2/{name}')
async def greet_name_both(name:str, age:int) -> dict:
    return {'msg':f'Hi {name}, {age}'}
# http://127.0.0.1:8000/greet2/dev?age=23

# Optional Query parameter
@app.get('/greet3')
# async def greet_name_query(name:str | None=None, age:int | None=None) -> dict:
async def greet_name_query(name:str, age:Optional[int] = 18) -> dict:
    return {'msg':f'Hello {name}, {age}'}
'''
Two ways -> 1. Optional[]    2. None = None
but cannot give default value in None = None
'''
"""
# ----------------------------------------------------------

"""
# ------- Request Body -------
class BookSchema(BaseModel):
    title : str
    author : str

@app.post('/create_book')
async def create_book(book_data:BookSchema):
    return {
        'title':book_data.title,
        'author':book_data.author
    }
"""

# ----------------------------------------------------------
"""
# --------- Headers ---------
@app.get('/get_headers')   #  , status_code=201
async def get_headers(
    accept:str = Header(None),
    content_type:str = Header(None),
    user_agent:str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content_type"] = content_type
    request_headers["User_agent"] = user_agent
    request_headers["Host"] = host
    return request_headers
    
"""