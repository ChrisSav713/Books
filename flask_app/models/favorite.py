from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']
        self.created_id = data['created_id']
        self.updated_id = data['updated_id']

    @classmethod
    def save(cls,data):
        query = '''
        INSERT INTO favorites (author_id, book_id, created_at, updated_at)
        VALUES ( %(author_id)s, %(book_id)s, NOW(), NOW() );
        '''
        return connectToMySQL("books_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_one(cls, data):
        pass

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def destroy(cls, data):
        pass

