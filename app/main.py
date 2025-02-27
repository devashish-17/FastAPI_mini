from fastapi import FastAPI, status, HTTPException
from typing import List
from src.books.book_data import books
from src.books.schemas import BookSchema, BookUpdateSchema

app = FastAPI()




@app.get('/books', response_model=List[BookSchema])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: BookSchema) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}')
async def get_a_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')

@app.patch('/book/{book_id}')
async def update_a_book(book_id:int, book_update_data:BookUpdateSchema) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')

@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')





