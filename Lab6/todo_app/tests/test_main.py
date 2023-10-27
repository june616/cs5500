from src.main import app
from fastapi.testclient import TestClient

# Create a test client
client = TestClient(app)

# Test the simple GET /api endpoint
def test_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}

# Test the /books/{path_para} endpoint
def test_get_book_by_id():
    book_id = "123"
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"msg": f"Get book with ID {book_id}"}

# Test the /books/ endpoint with query parameters
def test_get_books_by_title():
    title = "Python"
    response = client.get(f"/books/?title={title}")
    assert response.status_code == 200
    assert response.json() == {"msg": f"Get books with title: {title}"}

# Test the /books/{path_para}/query endpoint with both path and query parameters
def test_get_books_by_id_and_title():
    book_id = "123"
    title = "Python"
    response = client.get(f"/books/{book_id}/query", params={"title": title})
    assert response.status_code == 200
    assert response.json() == {"msg": f"Get book with ID {book_id} and title: {title}"}

# Test the /books/create_book endpoint (POST)
def test_create_book():
    new_book = {"title": "New Book", "author": "Author Name"}
    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"msg": "Created book", "book_data": new_book}

# Test the /books/update_book/{book_id} endpoint (PUT)
def test_update_book():
    book_id = 789
    updated_book = {"title": "Updated Book", "author": "Updated Author"}
    response = client.put(f"/books/update_book/{book_id}", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"msg": f"Updated book with ID {book_id}", "updated_data": updated_book}

# Test the /books/delete_book/{book_id} endpoint (DELETE)
def test_delete_book():
    book_id = 101
    response = client.delete(f"/books/delete_book/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"msg": f"Deleted book with ID {book_id}"}
