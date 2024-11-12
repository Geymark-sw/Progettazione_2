#app.py
from flask import Flask, jsonify

app = Flask(__name__)

#Lista di libri come esempio di dati
books = [
    {"id": 1, "title": "Il Nome della Rosa", "author": "Umberto Eco"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "Il Piccolo Principe", "author": "Antoine de Saint-Exupéry"}
]

@app.route('/')
def home():
    return """
    <h1>Benvenuto nella nostra libreria!</h1>
    <p>Usa <a href='/api/books'>/api/books</a> per vedere tutti i libri</p>
    <p>Usa /api/books/[id] per vedere un libro specifico</p>
    """

@app.route('/api/books')
def get_books():
    return jsonify(books)

@app.route('/api/books/<int:book_id>')
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Libro non trovato"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
