from databases import Database
from config import DB_NAME, DB_HOST, DB_PASS, DB_PORT, DB_USER


DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

database = Database(DATABASE_URL)

