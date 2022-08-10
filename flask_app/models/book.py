from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO books ( title, num_of_pages, created_at, updated_at )
        VALUES ( %(title)s, %(num_of_pages)s, NOW(), NOW() )
        '''
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book_item in results:
            books.append(cls(book_item))
        return books

    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * from books
        WHERE id = %(id)s;
        '''
        result = connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_authors(cls, data):
        query = '''
        SELECT authors.name
        FROM authors
        JOIN favorites on authors.id = favorites.author_id
        JOIN books on favorites.book_id = books.id
        WHERE books.id = (%(id)s);
        '''
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def destroy(cls, data):
        pass