from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO authors (name, created_at, updated_at)
        VALUES ( %(name)s, NOW(), NOW());
        '''
        return connectToMySQL("books_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author_item in results:
            authors.append(cls(author_item))
        return authors

    @classmethod
    def get_books(cls, data):
        query = '''
        SELECT books.title, books.num_of_pages
        FROM authors
        RIGHT JOIN favorites on authors.id = favorites.author_id
        RIGHT JOIN books on favorites.book_id = books.id
        WHERE authors.id = (%(id)s);
        '''
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * from authors
        WHERE id = %(id)s;
        '''
        result = connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def destroy(cls, data):
        pass
