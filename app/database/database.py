from databases import Database

DATABASE_URL = 'postgresql://user:oass@localhost/test'
database = Database(DATABASE_URL)
fake_db = {
    'categories': [],
    'articles': [],
    'users': []
}



