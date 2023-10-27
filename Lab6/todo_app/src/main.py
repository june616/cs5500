from fastapi import FastAPI, Body

app = FastAPI()

# Simple GET
@app.get("/api")
def api_get():
    return {"msg": "hello_world"}

# GET with path parameters
@app.get("/books/{path_para}")
def get_book_by_id(path_para: str):
    return {"msg": f"Get book with ID {path_para}"}

# GET with query parameters
@app.get("/books/")
def get_books_by_title(title: str):
    return {"msg": f"Get books with title: {title}"}

# GET with path parameters and query parameters
@app.get("/books/{path_para}/query")
def get_books_by_id_and_title(path_para: str, title: str):
    return {"msg": f"Get book with ID {path_para} and title: {title}"}

# POST
@app.post("/books/create_book")
def create_book(new_book=Body(...)):
    return {"msg": "Created book", "book_data": new_book}

# PUT
@app.put("/books/update_book/{book_id}")
def update_book(book_id: int, updated_book=Body(...)):
    return {"msg": f"Updated book with ID {book_id}", "updated_data": updated_book}

# DELETE
@app.delete("/books/delete_book/{book_id}")
def delete_book(book_id: int):
    return {"msg": f"Deleted book with ID {book_id}"}