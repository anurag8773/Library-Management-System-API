from flask import Flask, request, jsonify, abort
from datetime import datetime
import hashlib

app = Flask(__name__)

# In-memory storage
books = []
members = []
tokens = {}

# Helper: Check token validity
def is_token_valid(token):
    return token in tokens and tokens[token]['valid']

# Helper: Generate a unique token
def create_token(member_id):
    token = hashlib.sha256(f"{member_id}{datetime.now()}".encode()).hexdigest()
    tokens[token] = {"valid": True, "member_id": member_id}
    return token

# Book model
class Book:
    def __init__(self, title, author, isbn):
        self.id = len(books) + 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

# Member model
class Member:
    def __init__(self, name, email):
        self.id = len(members) + 1
        self.name = name
        self.email = email

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

# Routes
@app.route("/books", methods=["POST"])
def add_book():
    token = request.headers.get('Authorization')
    if not is_token_valid(token):
        abort(401, description="Unauthorized")

    data = request.get_json()
    book = Book(data['title'], data['author'], data['isbn'])
    books.append(book)
    return jsonify(book.to_dict()), 201

@app.route("/books", methods=["GET"])
def get_books():
    page = int(request.args.get('page', 1))
    start, end = (page - 1) * 5, page * 5
    return jsonify([book.to_dict() for book in books[start:end]])

@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = next((b for b in books if b.id == id), None)
    if not book:
        abort(404, description="Book not found")
    return jsonify(book.to_dict())

@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    token = request.headers.get('Authorization')
    if not is_token_valid(token):
        abort(401, description="Unauthorized")

    data = request.get_json()
    book = next((b for b in books if b.id == id), None)
    if not book:
        abort(404, description="Book not found")

    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.isbn = data.get("isbn", book.isbn)
    return jsonify(book.to_dict())

@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    token = request.headers.get('Authorization')
    if not is_token_valid(token):
        abort(401, description="Unauthorized")

    book = next((b for b in books if b.id == id), None)
    if not book:
        abort(404, description="Book not found")
    books.remove(book)
    return '', 204

@app.route("/books/search", methods=["GET"])
def search_books():
    title, author = request.args.get('title', '').lower(), request.args.get('author', '').lower()
    result = [book.to_dict() for book in books if title in book.title.lower() or author in book.author.lower()]
    return jsonify(result)

@app.route("/members", methods=["POST"])
def add_member():
    data = request.get_json()
    member = Member(data['name'], data['email'])
    members.append(member)
    return jsonify(member.to_dict()), 201

@app.route("/members/<int:id>", methods=["GET"])
def get_member(id):
    member = next((m for m in members if m.id == id), None)
    if not member:
        abort(404, description="Member not found")
    return jsonify(member.to_dict())

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data['email']
    member = next((m for m in members if m.email == email), None)
    if member:
        token = create_token(member.id)
        return jsonify({"token": token})
    abort(404, description="Member not found")

if __name__ == "__main__":
    app.run(debug=True)
