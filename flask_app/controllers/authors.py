from flask import Flask, render_template, redirect, request, url_for
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

@app.route('/')
def index():
    authors = Author.get_all()
    return render_template("authors.html",authors=authors)

@app.route('/create_author', methods=['GET', 'POST'])
def create_author():
    data = {
    "name": request.form['name']
    }
    Author.save(data)
    return redirect('/')

@app.route('/add_favorite', methods=['GET','POST'])
def add_favorite():
    data = {
        "author_id":request.form['author'],
        "book_id":request.form['book_id']
    }
    Favorite.save(data)
    original_author = request.form['author']
    return redirect(url_for('show_author',id=original_author))

@app.route('/add_favorite_author', methods=['GET','POST'])
def add_favorite_author():
    data = {
        "book_id":request.form['book'],
        "author_id":request.form['author_id']
    }
    Favorite.save(data)
    return redirect(url_for('show_book',id=request.form['book']))

@app.route('/author/<int:id>')
def show_author(id):
    data={'id':id}
    author_item = Author.get_one(data)
    books = Author.get_books(data)
    all_books = Book.get_all()
    return render_template("author.html", author_item=author_item, books=books, all_books=all_books)

@app.route('/create_book',methods=['GET','POST'])
def create_book():
    data = {
    "title": request.form['title'],
    "num_of_pages": request.form['num_of_pages']
    }
    Book.save(data)
    return redirect('/render_books')

@app.route('/render_books')
def render_books():
    books = Book.get_all()
    return render_template("books.html", books=books)

@app.route('/book/<int:id>')
def show_book(id):
    data={'id':id}
    book_item = Book.get_one(data)
    print(book_item)
    authors = Book.get_authors(data)
    all_authors = Author.get_all()
    return render_template("book.html", book_item=book_item, authors=authors, all_authors=all_authors)